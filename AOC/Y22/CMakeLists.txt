cmake_minimum_required(VERSION 3.10)
project(AOC)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/build)

include_directories(${CMAKE_SOURCE_DIR}/src)

add_executable(main
        src/main.cpp
        src/D1/sol1.cpp
        src/D2/sol2.cpp
        src/D3/sol3.cpp
        src/D4/sol4.cpp
        src/D5/sol5.cpp

        src/utils/utils.cpp
        src/D6/sol6.cpp
        src/D7/sol7.cpp
        src/D8/sol8.cpp
        src/D9/sol9.cpp
        src/D9/sol9.h
        src/D10/sol10.cpp
        src/D10/sol10.h
        src/D11/sol11.cpp
        src/D11/sol11.h
        src/D12/sol12.cpp
        src/D12/sol12.h
)

include(FetchContent)

FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/refs/heads/main.zip
        DOWNLOAD_EXTRACT_TIMESTAMP TRUE
)

# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(test_runner
        tests/test_sol1.cpp
        src/D1/sol1.cpp
)

target_link_libraries(test_runner gtest_main)

include(GoogleTest)
gtest_discover_tests(test_runner
        WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}/src"
)
