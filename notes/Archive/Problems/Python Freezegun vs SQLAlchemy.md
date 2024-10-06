---
subtitle: Freezefun Footgun
---
Freezegun is a python library designed to override datetime so that tests can run with consistent timestamps.  This works great in most cases, but can break when used with SQLAlchemy relationships.

If you use `func.current_date()` or `func.now()` from SQLAlchemy func, they will be generated in the [[Databases|database]] so won't respect the frozen datetime used by freezegun.

If you use datetime.now() an ORM model relationship like this:

```python
    user = db.relationship(
        "User",
        secondary=SiteOwnership.__table__,
        primaryjoin=lambda: and_(
            BaseSite.id == SiteOwnership.site_id,
            SiteOwnership.start_date <= datetime.now().date,
            ((SiteOwnership.end_date > datetime.now().date) | (SiteOwnership.end_date.is_(None))),
        ),
        order_by=(desc(SiteOwnership.updated_on)),
        uselist=False,
        overlaps="site_ownerships,user,site",
    )

```

the datetime will not be respected either. I wonder if this is because the `datetime.now().date` is invoked before freezegun is activated (during server setup).