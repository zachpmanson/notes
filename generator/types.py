from dataclasses import dataclass


@dataclass
class Node:
    parent: str | None
    children: set[str]

    title: str
    subtitle: str | None
    body: str
    rss_body: str

    backlinks: set[str]

    mod_date: str  # "2023-02-23 20:54:42 +0800%"
    creation_date: str  # "2023-02-23 20:54:42 +0800%"

    breadcrumb_path: str  # path in notes folder as string
    random_page: str  # random page when using static random
    script: str | None  # js to include
    post_date: str | None  # date used for chronological sorting

    children_visible: bool = True
