MPV's [infamous commit](https://github.com/mpv-player/mpv/commit/1e70e82baa9193f6f027338b0fab0f5078971fbe) explaining the myriad problems with C locales by contributor wm4.

---

```
commit 1e70e82baa9193f6f027338b0fab0f5078971fbe
Author: wm4 <wm4@nowhere>
Date:   Sun Nov 12 13:36:35 2017 +0100

    stream_libarchive: workaround various types of locale braindeath
    
    Fix that libarchive fails to return filenames for UTF-8/UTF-16 entries.
    The reason is that it uses locales and all that garbage, and mpv does
    not set a locale.
    
    Both C locales and wchar_t are shitfucked retarded legacy braindeath. If
    the C/POSIX standard committee had actually competent members, these
    would have been deprecated or removed long ago. (I mean, they managed to
    remove gets().) To justify this emotional outbreak potentially insulting
    to unknown persons, I will write a lot of text. Those not comfortable
    with toxic language should pretend this is a religious text.
    
    C locales are supposed to be a way to support certain languages and
    cultures easier. One example are character codepages. Back when UTF-8
    was not invented yet, there were only 255 possible characters, which is
    not enough for anything but English and some european languages. So they
    decided to make the meaning of a character dependent on the current
    codepage. The locale (LC_CTYPE specifically) determines what character
    encoding is currently used.
    
    Of course nowadays, this is legacy nonsense. Everything uses UTF-8 for
    "char", and what doesn't is broken and terrible anyway. But the old ways
    stayed with us, and the stupidity of it as well.
    
    C locales were utterly moronic even when they were invented. The locale
    (via setlocale()) is global state, and global state is not a reasonable
    way to do anything. It will break libraries, or well modularized code.
    (The latter would be forced to strictly guard all entrypoints set
    set/restore locales, assuming a single threaded world.)
    
    On top of that, setting a locale randomly changes the semantics of a
    bunch of standard functions. If a function respects locale, you suddenly
    can't rely on it to behave the same on all systems. Some behavior can
    come as a surprise, and of course it will be dependent on the region of
    the user (it doesn't help that most software is US-centric, and the US
    locale is almost like the C locale, i.e. almost what you expect).
    
    Idiotically, locales were not just used to define the current character
    encoding, but the concept was used for a whole lot of things, like e. g.
    whether numbers should use "," or "." as decimal separaror. The latter
    issue is actually much worse, because it breaks basic string conversion
    or parsing of numbers for the purpose of interacting with file formats
    and such.
    
    Much can be said about how retarded locales are, even beyond what I just
    wrote, or will wrote below. They are so hilariously misdesigned and
    insufficient, I can't even fathom how this shit was _standardized_. (In
    any case, that meant everyone was forced to implement it.) Many C
    functions can't even do it correctly. For example, the character set
    encoding can be a multibyte encoding (not just UTF-8, but awful garbage
    like Shift JIS (sometimes called SHIT JIZZ), yet functions like
    toupper() can return only 1 byte. Or just take the fact that the locale
    API tries to define standard paper sizes (LC_PAPER) or telephone number
    formatting (LC_TELEPHONE). Who the fuck uses this, or would ever use
    this?
    
    But the badness doesn't stop here. At some point, they invented threads.
    And they put absolutely no thought into how threads should interact with
    locales. So they kept locales as global state. Because obviously, you
    want to be able to change the semantics of basic string processing
    functions _while_ they're running, right? (Any thread can call
    setlocale() at any time, and it's supposed to change the locale of all
    other threads.)
    
    At this point, how the fuck are you supposed to do anything correctly?
    You can't even temporarily switch the locale with setlocale(), because
    it would asynchronously fuckup the other threads. All you can do is to
    enforce a convention not to set anything but the C local (this is what
    mpv does), or to duplicate standard functions using code that doesn't
    query locale (this is what e.g. libass does, a close dependency of mpv).
    
    Imagine they had done this for certain other things. Like errno, with
    all the brokenness of the locale API. This simply wouldn't have worked,
    shit would just have been too broken. So they didn't. But locales give a
    delicious sweet spot of brokenness, where things are broken enough to
    cause neverending pain, but not broken enough that enough effort would
    have spent to fix it completely.
    
    On that note, standard C11 actually can't stringify an error value. It
    does define strerror(), but it's not thread safe, even though C11
    supports threads. The idiots could just have defined it to be thread
    safe. Even if your libc is horrible enough that it can't return string
    literals, it could just just some thread local buffer. Because C11 does
    define thread local variables. But hey, why care about details, if you
    can just create a shitty standard?
    
    (POSIX defines strerror_r(), which "solves" this problem, while still
    not making strerror() thread safe.)
    
    Anyway, back to threads. The interaction of locales and threads makes no
    sense. Why would you make locales process global? Who even wanted it to
    work this way? Who decided that it should keep working this way, despite
    being so broken (and certainly causing implementation difficulties in
    libc)? Was it just a fucked up psychopath?
    
    Several decades later, the moronic standard committees noticed that this
    was (still is) kind of a bad situation. Instead of fixing the situation,
    they added more garbage on top of it. (Probably for the sake of
    "compatibility"). Now there is a set of new functions, which allow you
    to override the locale for the current thread. This means you can
    temporarily override and restore the local on all entrypoints of your
    code (like you could with setlocale(), before threads were invented).
    
    And of course not all operating systems or libcs implement this. For
    example, I'm pretty sure Microsoft doesn't. (Microsoft got to fuck it up
    as usual, and only provides _configthreadlocale(). This is shitfucked on
    its own, because it's GLOBAL STATE to configure that GLOBAL STATE should
    not be GLOBAL STATE, i.e. completely broken garbage, because it requires
    agreement over all modules/libraries what behavior should be used. I
    mean, sure, makign setlocale() affect only the current thread would have
    been the reasonable behavior. Making this behavior configurable isn't,
    because you can't rely on what behavior is active.)
    
    POSIX showed some minor decency by at least introducing some variations
    of standard functions, which have a locale argument (e.g. toupper_l()).
    You just pass the locale which you want to be used, and don't have to do
    the set locale/call function/restore locale nonense. But OF COURSE they
    fucked this up too. In no less than 2 ways:
    
    - There is no statically available handle for the C locale, so you have
      to initialize and store it somewhere, which makes it harder to make
      utility functions safe, that call locale-affected standard functions
      and expect C semantics. The easy solution, using pthread_once() and a
      global variable with the created locale, will not be easily accepted
      by pedantic assholes, because they'll worry about allocation failure,
      or leaking the locale when using this in library code (and then
      unloading the library). Or you could have complicated library
      init/uninit functions, which bring a big load of their own mess.
      Same for automagic DLL constructors/destructors.
    - Not all functions have a variant that takes a locale argument, and
      they missed even some important ones, like snprintf() or strtod() WHAT
      THE FUCK WHAT THE FUCK WHAT THE FUCK WHAT THE FUCK WHAT THE FUCK WHAT
      THE FUCK WHAT THE FUCK WHAT THE FUCK WHAT THE FUCK
    
    I would like to know why it took so long to standardize a half-assed
    solution, that, apart from being conceptually half-assed, is even
    incomplete and insufficient. The obvious way to fix this would have
    been:
    
    - deprecate the entire locale API and their use, and make it a NOP
    - make UTF-8 the standard character type
    - make the C locale behavior the default
    - add new APIs that explicitly take locale objects
    - provide an emulation layer, that can be used to transparently build
      legacy code without breaking them
    
    But this wouldn't have been "compatible", and the apparently incompetent
    standard committees would have never accepted this. As if anyone
    actually used this legacy garbage, except other legacy garbage. Oh yeah,
    and let's care a lot about legacy compatibility, and let's not care  at
    all about modern code that either has to suffer from this, or subtly
    breaks when the wrong locales are active.
    
    Last but not least, the UTF-8 locale name is apparently not even
    standardized. At the moment I'm trying to use "C.UTF-8", which is
    apparently glibc _and_ Debian specific. Got to use every opportunity to
    make correct usage of UTF-8 harder. What luck that this commit is only
    for some optional relatively obscure mpv feature.
    
    Why is the C locale not UTF-8? Why did POSIX not standardize an UTF-8
    locale? Well, according to something I heard a few years ago, they're
    considering disallowing UTF-8 as locale, because UTF-8 would violate
    certain ivnariants expected by C or POSIX. (But I'm not sure if I
    remember this correctly - probably better not to rage about it.)
    
    Now, on to libarchive.
    
    libarchive intentionally uses the locale API and all the broken crap
    around it to "convert" UTF-8 or UTF-16 (as contained in reasonably sane
    archive formats) to "char*". This is a good start!
    
    Since glibc does not think that the C locale uses UTF-8, this fails for
    mpv. So trying to use archive_entry_pathname() to get the archive entry
    name fails if the name contains non-ASCII characters.
    
    Maybe use archive_entry_pathname_utf8()? Surely that should return
    UTF-8, since its name seems to indicate that it returns UTF-8. But of
    fucking course it doesn't! libarchive's horribly convoluted code (that
    is full of locale API usage and other legacy shit, as well as ifdefs and
    OS specific code, including Windows and fucking Cygwin) somehow fucks up
    and fails if the locale is not set to UTF-8. I made a PR fixing this in
    libarchive almost 2 years ago, but it was ignored.
    
    So, would archive_entry_pathname_w() as fallback work? No, why would it?
    Of course this _also_ involves shitfucked code that calls shitfucked
    standard functions (or OS specific ifdeffed shitfuck). The truth is that
    at least glibc changes the meaning of wchar_t depending on the locale.
    Unlike most people think, wchar_t is not standardized to be an UTF
    variant (or even unicode) - it's an encoding that uses basic units that
    can be larger than 8 bit. It's an implementation defined thing. Windows
    defines it to 2 bytes and UTF-16, and glibc defines it to 4 bytes and
    UTF-32, but only if an UTF-8 locale is set (apparently).
    
    Yes. Every libarchive function dealing with strings has 3 variants:
    plain, _utf8, and _w. And none of these work if the locale is not set.
    I cannot fathom why they even have a wchar_t variant, because it's
    redundant and fucking useless for any modern code.
    
    Writing a UTF-16 to UTF-8 conversion routine is maybe 3 pages of code,
    or a few lines if you use iconv. But libarchive uses all this glorious
    bullshit, and ends up with 3 not working API functions, and with over
    4000 lines of its own string abstraction code with gratuitous amounts of
    ifdefs and OS dependent code that breaks in a fairly common use case.
    
    So what we do is:
    
    - Use the idiotic POSIX 2008 API (uselocale() etc.) (Too bad for users
      who try to build this on a system that doesn't have these - hopefully
      none are left in 2017. But if there are, torturing them with obscure
      build errors is probably justified. Might be bad for Windows though,
      which is a very popular platform except on phones.)
    - Use the "C.UTF-8" locale, which is probably not 100% standards
      compliant, but works on my system, so it's fine.
    - Guard every libarchive call with uselocale() + restoring the locale.
    - Be lazy and skip some libarchive calls. Look forward to the unlikely
      and astonishingly stupid bugs this could produce.
    
    We could also just set a C UTF-8 local in main (since that would have no
    known negative effects on the rest of the code), but this won't work for
    libmpv.
    
    We assume that uselocale() never fails. In an unexplainable stroke of
    luck, POSIX made the semantics of uselocale() nice enough that user code
    can fail failures without introducing crash or security bugs, even if
    there should be an implementation fucked up enough where it's actually
    possible that uselocale() fails even with valid input.
    
    With all this shitty ugliness added, it finally works, without fucking
    up other parts of the player. This is still less bad than that time when
    libquivi fucked up OpenGL rendering, because calling a libquvi function
    would load some proxy abstraction library, which in turn loaded a KDE
    plugin (even if KDE was not used), which in turn called setlocale()
    because Qt does this, and consequently made the mpv GLSL shader
    generation code emit "," instead of "." for numbers, and of course only
    for users who had that KDE plugin installed, and lived in a part of the
    world where "." is not used as decimal separator.
    
    All in all, I believe this proves that software developers as a whole
    and as a culture produce worse results than drug addicted butt fucked
    monkeys randomly hacking on typewriters while inhaling the fumes of a
    radioactive dumpster fire fueled by chinese platsic toys for children
    and Elton John/Justin Bieber crossover CDs for all eternity.

diff --git a/stream/stream_libarchive.c b/stream/stream_libarchive.c
index b4267e6ebb..fdcc9c3ce2 100644
--- a/stream/stream_libarchive.c
+++ b/stream/stream_libarchive.c
@@ -150,6 +150,8 @@ static bool mp_archive_check_fatal(struct mp_archive *mpa, int r)
 void mp_archive_free(struct mp_archive *mpa)
 {
     mp_archive_close(mpa);
+    if (mpa && mpa->locale)
+        freelocale(mpa->locale);
     talloc_free(mpa);
 }
 
@@ -229,7 +231,10 @@ static bool add_volume(struct mp_log *log, struct mp_archive *mpa,
     vol->mpa = mpa;
     vol->src = src;
     vol->url = talloc_strdup(vol, url);
-    return archive_read_append_callback_data(mpa->arch, vol) == ARCHIVE_OK;
+    locale_t oldlocale = uselocale(mpa->locale);
+    bool res = archive_read_append_callback_data(mpa->arch, vol) == ARCHIVE_OK;
+    uselocale(oldlocale);
+    return res;
 }
 
 struct mp_archive *mp_archive_new(struct mp_log *log, struct stream *src,
@@ -237,6 +242,9 @@ struct mp_archive *mp_archive_new(struct mp_log *log, struct stream *src,
 {
     struct mp_archive *mpa = talloc_zero(NULL, struct mp_archive);
     mpa->log = log;
+    mpa->locale = newlocale(LC_ALL_MASK, "C.UTF-8", (locale_t)0);
+    if (!mpa->locale)
+        goto err;
     mpa->arch = archive_read_new();
     mpa->primary_src = src;
     if (!mpa->arch)
@@ -256,6 +264,8 @@ struct mp_archive *mp_archive_new(struct mp_log *log, struct stream *src,
     }
     talloc_free(volumes);
 
+    locale_t oldlocale = uselocale(mpa->locale);
+
     archive_read_support_format_7zip(mpa->arch);
     archive_read_support_format_iso9660(mpa->arch);
     archive_read_support_format_rar(mpa->arch);
@@ -275,7 +285,11 @@ struct mp_archive *mp_archive_new(struct mp_log *log, struct stream *src,
     archive_read_set_close_callback(mpa->arch, close_cb);
     if (mpa->primary_src->seekable)
         archive_read_set_seek_callback(mpa->arch, seek_cb);
-    if (archive_read_open1(mpa->arch) < ARCHIVE_OK)
+    bool fail = archive_read_open1(mpa->arch) < ARCHIVE_OK;
+
+    uselocale(oldlocale);
+
+    if (fail)
         goto err;
     return mpa;
 
@@ -295,6 +309,9 @@ bool mp_archive_next_entry(struct mp_archive *mpa)
     if (!mpa->arch)
         return false;
 
+    locale_t oldlocale = uselocale(mpa->locale);
+    bool success = false;
+
     while (!mp_cancel_test(mpa->primary_src->cancel)) {
         struct archive_entry *entry;
         int r = archive_read_next_header(mpa->arch, &entry);
@@ -319,10 +336,13 @@ bool mp_archive_next_entry(struct mp_archive *mpa)
         mpa->entry = entry;
         mpa->entry_filename = talloc_strdup(mpa, fn);
         mpa->entry_num += 1;
-        return true;
+        success = true;
+        break;
     }
 
-    return false;
+    uselocale(oldlocale);
+
+    return success;
 }
 
 struct priv {
@@ -344,9 +364,11 @@ static int reopen_archive(stream_t *s)
     struct mp_archive *mpa = p->mpa;
     while (mp_archive_next_entry(mpa)) {
         if (strcmp(p->entry_name, mpa->entry_filename) == 0) {
+            locale_t oldlocale = uselocale(mpa->locale);
             p->entry_size = -1;
             if (archive_entry_size_is_set(mpa->entry))
                 p->entry_size = archive_entry_size(mpa->entry);
+            uselocale(oldlocale);
             return STREAM_OK;
         }
     }
@@ -362,6 +384,7 @@ static int archive_entry_fill_buffer(stream_t *s, char *buffer, int max_len)
     struct priv *p = s->priv;
     if (!p->mpa)
         return 0;
+    locale_t oldlocale = uselocale(p->mpa->locale);
     int r = archive_read_data(p->mpa->arch, buffer, max_len);
     if (r < 0) {
         MP_ERR(s, "%s\n", archive_error_string(p->mpa->arch));
@@ -370,6 +393,7 @@ static int archive_entry_fill_buffer(stream_t *s, char *buffer, int max_len)
             p->mpa = NULL;
         }
     }
+    uselocale(oldlocale);
     return r;
 }
 
@@ -378,7 +402,9 @@ static int archive_entry_seek(stream_t *s, int64_t newpos)
     struct priv *p = s->priv;
     if (!p->mpa)
         return -1;
+    locale_t oldlocale = uselocale(p->mpa->locale);
     int r = archive_seek_data(p->mpa->arch, newpos, SEEK_SET);
+    uselocale(oldlocale);
     if (r >= 0)
         return 1;
     if (mp_archive_check_fatal(p->mpa, r)) {
@@ -404,15 +430,18 @@ static int archive_entry_seek(stream_t *s, int64_t newpos)
                 return -1;
 
             int size = MPMIN(newpos - s->pos, sizeof(buffer));
+            oldlocale = uselocale(p->mpa->locale);
             r = archive_read_data(p->mpa->arch, buffer, size);
             if (r < 0) {
                 MP_ERR(s, "%s\n", archive_error_string(p->mpa->arch));
+                uselocale(oldlocale);
                 if (mp_archive_check_fatal(p->mpa, r)) {
                     mp_archive_free(p->mpa);
                     p->mpa = NULL;
                 }
                 return -1;
             }
+            uselocale(oldlocale);
             s->pos += r;
         }
     }
diff --git a/stream/stream_libarchive.h b/stream/stream_libarchive.h
index c15dc1b528..939d6fa65a 100644
--- a/stream/stream_libarchive.h
+++ b/stream/stream_libarchive.h
@@ -1,6 +1,9 @@
+#include <locale.h>
+
 struct mp_log;
 
 struct mp_archive {
+    locale_t locale;
     struct mp_log *log;
     struct archive *arch;
     struct stream *primary_src;

```

