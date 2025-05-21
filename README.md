# The Rust Books

[![TRPL](https://github.com/containerpi/rsdocs-actions/actions/workflows/trpl.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/trpl.yaml)
[![tlborm](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/tlborm.yaml)
[![rustwasm](https://github.com/containerpi/rsdocs-actions/actions/workflows/rustwasm.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rustwasm.yaml)
[![rust-embedded](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-embedded.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-embedded.yaml)
[![async-book](https://github.com/containerpi/rsdocs-actions/actions/workflows/async-book.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/async-book.yaml)
[![perf-book](https://github.com/containerpi/rsdocs-actions/actions/workflows/perf-book.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/perf-book.yaml)
[![edition-guide](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml)
[![cheats.rs](https://github.com/containerpi/rsdocs-actions/actions/workflows/cheats-rs.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/cheats-rs.yaml)
[![rust-course](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-course.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-course.yaml)
[![learning-rust-by-practice](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-by-practice.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-by-practice.yaml)
[![the-rust-edition-guide](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/edition-guide.yaml)
[![actix-web](https://github.com/containerpi/rsdocs-actions/actions/workflows/actix-web.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/actix-web.yaml)
[![cargo](https://github.com/containerpi/rsdocs-actions/actions/workflows/cargo.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/cargo.yaml)
[![rust-guide](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-guide.yaml/badge.svg)](https://github.com/containerpi/rsdocs-actions/actions/workflows/rust-guide.yaml)

## Requirements

Building the book requires [mdBook], ideally the same version that
rust-lang/rust uses in [this file][rust-mdbook].

[mdBook]: https://github.com/rust-lang-nursery/mdBook
[rust-mdbook]: https://github.com/rust-lang/rust/blob/master/src/tools/rustbook/Cargo.toml

## Book List(China mirror) - auto build with github actions

| Name | Language | Comment(fork from) |
|:- |:- |:- |
|[The Rust Programming Language(2021 edition)](http://opendocs.containerpi.com/trpl/en) | en | [@rust-lang](https://github.com/rust-lang/book)|
|[Rust 程序设计语言(2021 edition)](http://opendocs.containerpi.com/trpl/zh) | zh | [@KaiserY](https://github.com/KaiserY/trpl-zh-cn)|
|[The Little Book of Rust Macros](http://opendocs.containerpi.com/tlborm/en/) | en | [@Veykril](https://github.com/Veykril/tlborm) |
|[Rust 宏小册](http://opendocs.containerpi.com/tlborm/zh/) | zh | [@zjp-CN](https://github.com/zjp-CN/tlborm) |
|[The Rust and WebAssembly Book](http://opendocs.containerpi.com/rustwasm/en/) | en | [@rustwasm](https://github.com/rustwasm/book) |
|[The Embedded Rust Book](http://opendocs.containerpi.com/rust-embedded/en/) | en | [@rust-embedded](https://github.com/rust-embedded/book) |
|[Asynchronous Programming in Rust](http://opendocs.containerpi.com/async-book/en/) | en | [@rust-lang](https://github.com/rust-lang/async-book) |
|[The Rust Performance Book](http://opendocs.containerpi.com/perf-book/en/) | en | [@rust-lang](https://github.com/nnethercote/perf-book) |
|[The Rust Edition Guide](http://opendocs.containerpi.com/edition-guide/en/) | en | [@rust-lang](https://github.com/rust-lang/edition-guide) |
|[Learn Rust with examples](http://opendocs.containerpi.com/rust-by-example/en/) | en | [@rust-lang](https://github.com/rust-lang/rust-by-example) |
|[通过例子学 Rust](http://opendocs.containerpi.com/rust-by-example/zh/) | zh | [@rust-lang-cn](https://github.com/rust-lang-cn/rust-by-example-cn) |
|[Rust Language Cheat Sheet](http://opendocs.containerpi.com/cheats.rs/en/) | en | [@ralfbiedert](https://github.com/ralfbiedert/cheats.rs) |
|[Rust 语言备忘清单（简体中文）](http://opendocs.containerpi.com/cheats.rs/zh/) | zh | [@kingfree](https://github.com/kingfree/cheats.rs/) |
|[A Rust Cookbook](http://opendocs.containerpi.com/rust-cookbook/en/) | en | [@rust-lang-nursery](https://github.com/rust-lang-nursery/rust-cookbook) |
|[Rust语言圣经 (The Course)](http://opendocs.containerpi.com/rust-course/zh/) | zh | [@sunface](https://github.com/sunface/rust-course) |
|[Learning Rust By Practice](http://opendocs.containerpi.com/rust-by-practice/en/) | en | [@sunface](https://github.com/sunface/rust-by-practice) |
|[Rust 练习实践](http://opendocs.containerpi.com/rust-by-practice/zh/) | zh | [@sunface](https://github.com/sunface/rust-by-practice/blob/master/zh-CN/src/why-exercise.md) |
|[Rust Cargo 官书（非官方翻译)](http://opendocs.containerpi.com/cargo/zh/) | zh | [@chinanf-boy](https://github.com/chinanf-boy/cargo-book-zh) |
|[The Cargo Book](http://opendocs.containerpi.com/cargo/en/) | en | [@rust-lang](https://github.com/rust-lang/cargo) |
|[actix-web 中文文档](http://opendocs.containerpi.com/actix-web/zh/) | zh | [@zzy](https://github.com/zzy/actix-web-zh-cn) |
|[Rust 实践指南](http://opendocs.containerpi.com/rust-guide/zh/) | zh | [@sunface](https://github.com/zzy/rust-guide) |
|[Comprehensive Rust](http://opendocs.containerpi.com/comprehensive-rust/en/) | en | [@google](https://github.com/google/comprehensive-rust) |
|[Rustup: the Rust toolchain installer](http://opendocs.containerpi.com/rustup/en/) | en | [@rust-lang](https://github.com/rust-lang/rustup) |
|[PyO3 user guide](http://opendocs.containerpi.com/pyo3/en/) | en | [@PyO3](https://github.com/PyO3/pyo3) |
|[Learn Rust Easy](http://opendocs.containerpi.com/Learn-rust-easy/zh/) | zh | [@令狐壹冲](https://github.com/RustyCab/LearnRustEasy) |

* Embedded Rust on Espressif ([en](http://opendocs.containerpi.com/std-training/en/) / [zh](http://opendocs.containerpi.com/std-training/zh/))
* The Rust on ESP Book ([en](http://opendocs.containerpi.com/rust-on-esp/en/) / [zh](http://opendocs.containerpi.com/rust-on-esp/zh/))
* impl Rust for ESP32 ([en](http://opendocs.containerpi.com/esp32-book/en/) / zh)

## Notes

* Run every day at 6:00 AM UTC
* Triggered manually

## Contribute

* Use [issues](https://github.com/containerpi/rsdocs-actions/issues) for everything
