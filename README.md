# The Rust Books

![Build for TRPL](https://github.com/containerpi/trpl-actions/workflows/Build%20for%20TRPL/badge.svg)
[![Build for Tlborm](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml)
[![Build for Rustwasm](https://github.com/containerpi/rsdocs-actions/actions/workflows/rustwasm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rustwasm.yaml)
[![Build for rust-embedded](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-embedded.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-embedded.yaml)
[![Build for async-book](https://github.com/containerpi/rsdocs-actions/actions/workflows/async-book.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/async-book.yaml)
[![Build for perf-book](https://github.com/containerpi/rsdocs-actions/actions/workflows/perf-book.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/perf-book.yaml)
[![Build for edition-guide](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml)


## Requirements

Building the book requires [mdBook], ideally the same version that
rust-lang/rust uses in [this file][rust-mdbook].

[mdBook]: https://github.com/rust-lang-nursery/mdBook
[rust-mdbook]: https://github.com/rust-lang/rust/blob/master/src/tools/rustbook/Cargo.toml

## Book List(China mirror) - auto build with github actions

| Name | Language | Comment(fork from) |
|:- |:- |:- |
|[The Rust Programming Language](http://docs.clset.com/trpl/en) | en | [@rust-lang](https://github.com/rust-lang/book)|
|[Rust 程序设计语言(第二版 & 2018 edition)](http://docs.clset.com/trpl/zh) | zh | [@KaiserY](https://github.com/KaiserY/trpl-zh-cn)|
|[The Little Book of Rust Macros](http://docs.clset.com/tlborm/en/) | en | [@Veykril](https://github.com/Veykril/tlborm) |
|[Rust 宏小册](http://docs.clset.com/tlborm/zh/) | zh | [@zjp-CN](https://github.com/zjp-CN/tlborm) |
|[The Rust and WebAssembly Book](http://docs.clset.com/rustwasm/en/) | en | [@rustwasm](https://github.com/rustwasm/book) |
|[The Embedded Rust Book](http://docs.clset.com/rust-embedded/en/) | en | [@rust-embedded](https://github.com/rust-embedded/book) |
|[Asynchronous Programming in Rust](http://docs.clset.com/async-book/en/) | en | [@rust-lang](https://github.com/rust-lang/async-book) |
|[The Rust Performance Book](http://docs.clset.com/perf-book/en/) | en | [@rust-lang](https://github.com/nnethercote/perf-book) |
|[A guide to changes between various editions of Rust](http://docs.clset.com/edition-guide/en/) | en | [@rust-lang](https://github.com/rust-lang/edition-guide) |


## Notes

* Run every day at 6:00 AM UTC
* Triggered manually


## Contribute

* Use [issues](https://github.com/containerpi/rsdocs-actions/issues) for everything
