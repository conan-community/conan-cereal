cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(Cereal CONFIG REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example ${CONAN_LIBS})
set_target_properties(example PROPERTIES CXX_STANDARD 11)
