Wherever possible, collect all the data you need first, then operate on it. Do not lazy load mid-calculation, one off database queries will inevitably be called 500 times consecutively by someone else paying less attention.

This also means testing is easier, as you can create all your test data outside of your services, and pass the data in whole.
