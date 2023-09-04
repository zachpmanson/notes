A statically typed, compiled programming language designed by Google designed to blend high performance networking, concurrency, memory safety and readability.  It was first created in 2009 by Robert Griesemer, [[Rob Pike's Lesson in Shortcuts|Rob Pike]] ([[Unix]], Plan 9, UTF-8) and Ken Thompson ([[C]], Unix).

It was borne from criticisms in other languages being used by Google at the time, with a particular shared dislike of C++.

## Variables

Variables are 0 initialised, `false` for bool and `""` for strings.  Explicit types are used with the `var name type` 

```go
// explicit typing
var name string
name = "text"

// duck typing
name2 := "text"

const pi = 3.14
```

## Types

Basic types:

```go
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```

Casting:

```
i := 42
f := float64(i)
u := uint(f)
```

Type definitions:

```go
type Page struct {
	Title string
	Body  []byte
}
```

## Control Structures

### `if`

```go
func pow(x, n, lim float64) float64 {
	// if
	if x < 0 {
		return sqrt(-x) + "i"
	} 

	// if with prefix statement
	if v := math.Pow(x, n); v < lim {
		// v is only in if scope
		return v
	}
}
```

### `for`

```go
func main() {
	sum := 0
	// for loop
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)

	// while loop
	for sum < 1000 {
		sum += sum
	}

	// infinite loop
	for {
		fmt.Println(sum)
	}
}
```

### `switch`

```go
func main() {
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}

	// conditionaless switch for clean else if chains
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```

## Interesting Constructs

Defer runs immediately after the function returns. The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

```go
func main() {
	defer fmt.Println("world")
	fmt.Println("hello")
}
```