#include "pch.h"
#include "../../StaticLib1/StaticLib1/framework.h"

TEST(TestCaseName, TestName) {
  EXPECT_EQ(simple(13), 1);
  EXPECT_TRUE(simple(13));
  EXPECT_EQ(nextSimple(13), 17);
  EXPECT_TRUE(simple(14));
}