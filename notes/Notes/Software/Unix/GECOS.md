When creating a new user account using the `adduser` program on Unix machines there is a field called GECOS that conventionally used to store information about the user, such as their real name or phone number.

```
adduser 
	[options] 
	[--home DIR]
	[--shell SHELL]
	[--no-create-home]
	[--uid ID]
	[--firstuid ID]
	[--lastuid ID]
	[--ingroup GROUP | --gid  ID] 
	[--disabled-password] 
	[--disabled-login]
	[--gecos GECOS]
	[--add_extra_groups]
	[--encrypt-home] user

--gecos GECOS
Set  the  gecos  field for the new entry generated.  adduser will not ask for finger 
information if this option is given.
```

The cryptic title is not explained in the man pages.  This field is called GECOS as it was originally used to describe the purpose of machines running the [General Electric Comprehensive Operating System](https://en.wikipedia.org/wiki/General_Comprehensive_Operating_System) (GECOS), which had user accounts set up to access the services running on those machines, such as print spooling.  This field was added to `/etc/passwd`, and was later repurposed to contain identifying information on each user.  This anachronism has managed to persist into modern Unix and Linux system to this day.

Tags: #unix #linux