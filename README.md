# The Rust Programming Language

![Build for TRPL](https://github.com/containerpi/trpl-actions/workflows/Build%20for%20TRPL/badge.svg)

This repository contains the source of "The Rust Programming Language" book.

[The book is available in dead-tree form from No Starch Press][nostarch].

[nostarch]: https://nostarch.com/rust

You can also read the book for free online. Please see the book as shipped with
the latest [stable], [beta], or [nightly] Rust releases. Be aware that issues
in those versions may have been fixed in this repository already, as those
releases are updated less frequently.

[stable]: https://doc.rust-lang.org/stable/book/
[beta]: https://doc.rust-lang.org/beta/book/
[nightly]: https://doc.rust-lang.org/nightly/book/

See the [releases] to download just the code of all the code listings that appear in the book.

[releases]: https://github.com/rust-lang/book/releases

## Requirements

Building the book requires [mdBook], ideally the same version that
rust-lang/rust uses in [this file][rust-mdbook].

[mdBook]: https://github.com/rust-lang-nursery/mdBook
[rust-mdbook]: https://github.com/rust-lang/rust/blob/master/src/tools/rustbook/Cargo.toml

## Book List(China mirror) - auto build with github actions

* [trpl en](http://docs.clset.com/trpl/en)
* [trpl zh](http://docs.clset.com/trpl/zh)  (Auto fetch from [@KaiserY](https://github.com/KaiserY/trpl-zh-cn), thanks.)

## Build schedule

* Run every friday at 6:00 AM UTC
* Triggered manually
