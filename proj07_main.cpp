#include <vector>
using std::vector;
#include <iostream>
using std::cout; using std::endl;
#include "proj07_functions.h"

vector<string> v{"hello", "my", "name", "is", "Heather"};
map_type a;
map_type b;
int main(){
    process_words(a, "example1_file.txt");
    print_map(cout, a);
}//end of main