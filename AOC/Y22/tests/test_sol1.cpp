//
// Copyright 2025 Fabian Stiewe
//

#include <gtest/gtest.h>

#include "D1/sol1.h"

TEST(Sol1Test, CompilesAndRuns) {
  solve();    // if it compiles and doesn't crash, test passes
  SUCCEED();  // explicitly mark this as a successful test
}
