#include <iostream>
using namespace std;

extern "C" {
    const char* hello(const char* name) {
        static string data = "this is hello from " + string(name);
        return data.c_str();
    }
}