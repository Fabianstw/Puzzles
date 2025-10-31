#!/bin/bash

echo "Checking code quality and running tests..."
echo "======================================================"

# Reconfiguring CMake
echo "🔁 Reconfiguring CMake..."
cmake -S . -B cmake-build-debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON > /dev/null 2>&1

# Build the project
echo "🔨 Building the project..."
cmake --build cmake-build-debug > /dev/null 2>&1  # Suppress regular output

# Formatting code with clang-format
echo "🔧 Formatting code with clang-format..."
# shellcheck disable=SC2038
find src tests \( -name '*.cpp' -o -name '*.h' \) | xargs clang-format -i  # Show processing files

echo ""
echo "======================================================"

# Running cpplint
echo "🧼 Running cpplint..."
# shellcheck disable=SC2038
find src tests \( -name '*.cpp' -o -name '*.h' \) | xargs cpplint --linelength=80

echo ""
echo "======================================================"

# Running clang-tidy
echo "🔍 Running clang-tidy..."
# shellcheck disable=SC2038
find src tests -name '*.cpp' | xargs clang-tidy -p cmake-build-debug

echo ""
echo "======================================================"

echo "🕵️ Running cppcheck..."
echo "Currently disabled due to false positives"
#cppcheck --enable=all --inconclusive --std=c++20 -I src/ src/

echo ""
echo "======================================================"

# Build tests
echo "🧪 Building tests..."
cmake --build cmake-build-debug --target test_runner > /dev/null 2>&1  # Only errors

# Run tests with working directory set to src
echo "🔧 Running tests with working directory set to src..."
(cd src && ../build/test_runner)
