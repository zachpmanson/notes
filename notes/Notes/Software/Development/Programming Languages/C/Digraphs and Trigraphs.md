[[C]] uses the preprocessor to substitute trigraphs for certain characters that did not appear on all keyboards in the 70s.

|Trigraph|Equivalent|
|---|---|
|`??=`|`#`|
|`??/`|`\`|
|`??'`|`^`|
|`??(`|`[`|
|`??)`|`]`|
|`??!`|`\|`|
|`??<`|`{`|
|`??>`|`}`|
|`??-`|`~`|

The can accidentally be triggered causing strange behaviour. 

```C
// Will the next line be executed????????????????/
a++;
```

`??/` gets converted to `\` so the comment gets extended to the second line when trigraphs are applied.

This can be used to check if trigraphs are available:

```c
int trigraphsavailable() // returns 0 or 1; language standard C99 or later
{
	// are trigraphs available??/
	return 0;
	return 1;
}
```

C99 added some digraphs that were more readable than the original trigraphs.

|Digraph|Equivalent|
|---|---|
|`<:`|`[`|
|`:>`|`]`|
|`<%`|`{`|
|`%>`|`}`|
|`%:`|`#`|

Trigraphs were removed in C23.