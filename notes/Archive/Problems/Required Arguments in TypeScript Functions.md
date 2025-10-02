---
tags:
  - relics
---

This will compile in [[TypeScript]]:

```ts
type Func = (arg1: number, arg2: string) => void;

const F: Func = (arg1) => {
  console.log(arg1);
};

F(1, "hello");

```


This is historical baggage from a [[footguns|footgun]] in the way [[JavaScript]] handles function arguments. This is historical baggage of JavaScript being made in ten days.

The only way to have TypeScript enforce parameters properly you need to use an object as the parameter type.

The following will (thankfully) fail to compile:

```ts
type Func = ({arg1: number; arg2: string}) => void;

const F: Func = ({ arg1 }) => {
  console.log(arg1);
};

F({ arg1: 1, arg2: "hello"});
```
