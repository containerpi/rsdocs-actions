# The Rust Books

## Requirements

Building the book requires [mdBook], ideally the same version that
rust-lang/rust uses in [this file][rust-mdbook].

[mdBook]: https://github.com/rust-lang-nursery/mdBook
[rust-mdbook]: https://github.com/rust-lang/rust/blob/master/src/tools/rustbook/Cargo.toml

## Book List(China mirror) - auto build with github actions

| Name | State | Comment |
|:- |:- |:- |
|[The Rust Programming Language](http://docs.clset.com/trpl/en) | ![Build for TRPL](https://github.com/containerpi/trpl-actions/workflows/Build%20for%20TRPL/badge.svg) | Fork from [@rust-lang/book](https://github.com/rust-lang/book)|
|[Rust 程序设计语言(第二版 & 2018 edition)](http://docs.clset.com/trpl/zh) | ![Build for TRPL](https://github.com/containerpi/trpl-actions/workflows/Build%20for%20TRPL/badge.svg) | Auto fetch from [@KaiserY](https://github.com/KaiserY/trpl-zh-cn)|
|[The Little Book of Rust Macros](http://docs.clset.com/tlborm/en/) | [![Build for Tlborm](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml) | Fork from [@Veykril](https://github.com/Veykril/tlborm) |
|[Rust 宏小册](http://docs.clset.com/tlborm/zh/) | [![Build for Tlborm](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml) | Auto fetch from [@zjp-CN](https://github.com/zjp-CN/tlborm) |


## Notes

* Run every day at 6:00 AM UTC
* Triggered manually
