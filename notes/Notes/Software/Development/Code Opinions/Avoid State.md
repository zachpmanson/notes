---
subtitle: Don't add state if you don't need to
---

Every possible state you add is something you need to remember to account for. It also becomes something every future dev will need to remember to account for. Keep state variables as minimal as possible, especially when dealing with classes. If you are using a class as a namespace sure I guess that makes sense, but those methods better all be static.

If I see something like this `cost = CostCalculator(start_date).calculate_costs_v2(data, end_date)` I’m gonna be mad.
