#ifndef IDK
#define IDK
#pragma once

#include<string>
using std::string;

string lower_case(const string&);
string to_binary(char);
char from_binary(const string&);
bool check_message(const string&, const string&);
string encode(const string&, const string&);
string decode(const string&);

#endif