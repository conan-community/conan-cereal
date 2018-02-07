from conans import ConanFile, CMake, tools
import os


class CerealConan(ConanFile):
    name = "cereal"
    version = "1.2.2"
    description = "Serialization header-only library for C++11."
    license = "BSD-3"
    no_copy_source = True
    source_subfolder = "sources"
    url = "https://github.com/USCiLab/cereal"

    def source(self):
        source_url = ("%s/archive/v%s.zip" % (self.url, self.version))
        tools.get(source_url)
        os.rename("%s-%s" % (self.name, self.version, ), self.source_subfolder)

    def package(self):
        src_include = os.path.join(self.source_subfolder, "include")
        self.copy("*.h", dst="include", src=src_include)
        self.copy("*.hpp", dst="include", src=src_include)
        self.copy("*LICENSE*", dst="licenses", src=self.source_subfolder)

    def package_id(self):
        self.info.header_only()
