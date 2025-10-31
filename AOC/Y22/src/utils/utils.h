//
// Copyright Fabian Stiewe
//
#pragma once

#include <iostream>
#include <string>
#include <vector>

#ifndef UTILS_H
#define UTILS_H

std::vector<std::string> splitString(const std::string& str,
                                     const std::string& delimiter);
std::vector<std::string> readFile(const std::string& filename);

#endif  // UTILS_H
