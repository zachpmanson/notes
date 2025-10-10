---
subtitle: back_populates is better than backref
---
Yes, `backref` is more concise, but it also creates attributes that only exist during runtime. I want to see every attribute (and type) in the code as I am writing it.

[Even SQLAlchemy docs advise `back_populates` over `backref`.](https://docs.sqlalchemy.org/en/14/orm/backref.html)