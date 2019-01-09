# Conan Cereal

![conan-cereal image](/images/conan-cereal.png)

[Conan.io](https://conan.io) package for [cereal](https://github.com/USCiLab/cereal) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/cereal%3Aconan).

| Bintray | Appveyor | Travis |
|---------|-----------|--------|
|[![Download](https://api.bintray.com/packages/conan-community/conan/cereal%3Aconan/images/download.svg) ](https://bintray.com/conan-community/conan/cereal%3Aconan/_latestVersion)|[![Build status](https://ci.appveyor.com/api/projects/status/github/ConanCIintegration/conan-cereal?svg=true)](https://ci.appveyor.com/project/ConanCIintegration/conan-cereal)|[![Build Status](https://travis-ci.org/conan-community/conan-cereal.svg)](https://travis-ci.org/conan-community/conan-cereal)|



## Basic setup

    $ conan install cereal/1.2.2@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    cereal/1.2.2@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
