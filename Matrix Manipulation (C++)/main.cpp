#include <vector>
using std::vector;
#include <iostream>
using std::cout; using std::endl;

#include "proj06_functions.h"

int main(){
vector<long> v {11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45};
long rows = 4;
long cols = 5;

long ans = 112;
long result = four_corner_sum(v,rows,cols);
cout << result << endl;
//print_vector(result, cout) <<endl;
}//main