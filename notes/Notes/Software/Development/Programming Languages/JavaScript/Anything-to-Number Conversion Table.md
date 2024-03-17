---
tags:
  - javascript
---
I found this [on StackOverflow](https://stackoverflow.com/a/17106702) by georg.

---

|x|parseInt(x)|parseFloat(x)|Number(x)|+x|~~x|x>>>0|isNaN(x)|
|---|---|---|---|---|---|---|---|
|"123"|123|123|123|123|123|123|false|
|"+123"|123|123|123|123|123|123|false|
|"-123"|-123|-123|-123|-123|-123|4294967173|false|
|"123.45"|123|123.45|123.45|123.45|123|123|false|
|"-123.45"|-123|-123.45|-123.45|-123.45|-123|4294967173|false|
|"12e5"|12|1200000|1200000|1200000|1200000|1200000|false|
|"12e-5"|12|0.00012|0.00012|0.00012|0|0|false|
|"0123"|123|123|123|123|123|123|false|
|"0000123"|123|123|123|123|123|123|false|
|"0b111"|0|0|7|7|7|7|false|
|"0o10"|0|0|8|8|8|8|false|
|"0xBABE"|47806|0|47806|47806|47806|47806|false|
|"4294967295"|4294967295|4294967295|4294967295|4294967295|-1|4294967295|false|
|"123456789012345678"|123456789012345680|123456789012345680|123456789012345680|123456789012345680|-1506741424|2788225872|false|
|"12e999"|12|Infinity|Infinity|Infinity|0|0|false|
|""|**NaN**|**NaN**|0|0|0|0|false|
|"123foo"|123|123|**NaN**|**NaN**|0|0|**true**|
|"123.45foo"|123|123.45|**NaN**|**NaN**|0|0|**true**|
|" 123 "|123|123|123|123|123|123|false|
|"foo"|**NaN**|**NaN**|**NaN**|**NaN**|0|0|**true**|
|"12e"|12|12|**NaN**|**NaN**|0|0|**true**|
|"0b567"|0|0|**NaN**|**NaN**|0|0|**true**|
|"0o999"|0|0|**NaN**|**NaN**|0|0|**true**|
|"0xFUZZ"|15|0|**NaN**|**NaN**|0|0|**true**|
|"+0"|0|0|0|0|0|0|false|
|"-0"|0|0|0|0|0|0|false|
|"Infinity"|**NaN**|Infinity|Infinity|Infinity|0|0|false|
|"+Infinity"|**NaN**|Infinity|Infinity|Infinity|0|0|false|
|"-Infinity"|**NaN**|-Infinity|-Infinity|-Infinity|0|0|false|
|BigInt(1)|1|1|1|**Error**|1|**Error**|**Error**|
|null|**NaN**|**NaN**|0|0|0|0|false|
|undefined|**NaN**|**NaN**|**NaN**|**NaN**|0|0|**true**|
|true|**NaN**|**NaN**|1|1|1|1|false|
|false|**NaN**|**NaN**|0|0|0|0|false|
|Infinity|**NaN**|Infinity|Infinity|Infinity|0|0|false|
|NaN|**NaN**|**NaN**|**NaN**|**NaN**|0|0|**true**|
|{}|**NaN**|**NaN**|**NaN**|**NaN**|0|0|**true**|
|{valueOf: function(){return 42}}|**NaN**|**NaN**|42|42|42|42|false|
|{toString: function(){return "56"}}|56|56|56|56|56|56|false|
And the JavaScript to generate it!

```javascript
EXPRS = [
    'parseInt(x)',
    'parseFloat(x)',
    'Number(x)',
    '+x',
    '~~x',
    'x>>>0',
    'isNaN(x)'

];

VALUES = [
    '"123"',
    '"+123"',
    '"-123"',
    '"123.45"',
    '"-123.45"',
    '"12e5"',
    '"12e-5"',
    
    '"0123"',
    '"0000123"',
    '"0b111"',
    '"0o10"',
    '"0xBABE"',
    
    '"4294967295"',
    '"123456789012345678"',
    '"12e999"',

    '""',
    '"123foo"',
    '"123.45foo"',
    '"  123   "',
    '"foo"',
    '"12e"',
    '"0b567"',
    '"0o999"',
    '"0xFUZZ"',

    '"+0"',
    '"-0"',
    '"Infinity"',
    '"+Infinity"',
    '"-Infinity"',
    'BigInt(1)',

    'null',
    'undefined',
    'true',
    'false',
    'Infinity',
    'NaN',

    '{}',
    '{valueOf: function(){return 42}}',
    '{toString: function(){return "56"}}',

];

//////

function wrap(tag, s) {
    if (s && s.join)
        s = s.join('');
    return '<' + tag + '>' + String(s) + '</' + tag + '>';
}

function table(head, rows) {
    return wrap('table', [
        wrap('thead', tr(head)),
        wrap('tbody', rows.map(tr))
    ]);
}

function tr(row) {
    return wrap('tr', row.map(function (s) {
        return wrap('td', s)
    }));
}

function val(n) {
    return n === true || Number.isNaN(n) || n === "Error" ? wrap('b', n) : String(n);
}

var rows = VALUES.map(function (v) {
    var x = eval('(' + v + ')');
    return [v].concat(EXPRS.map(function (e) {
        try {
            return val(eval(e));
        } catch {
            return val("Error");
        }
    }));
});

document.body.innerHTML = table(["x"].concat(EXPRS), rows);
```