#pragma once
#include<iostream>
using std::ostream;
#include<vector>
using std::vector;

ostream& print_vector(const vector<long>&, ostream&);
long four_corner_sum(const vector<long>&, int,int);
vector<long> rotate_rows_up(const vector<long>&, int, int);
vector<long> column_order(const vector<long>&, int, int);
vector<long> matrix_ccw_rotate(const vector<long>&, int, int);
long max_column_diff(const vector<long>&, int, int);  
bool check_neighbors(const vector<long>& v, int rows, int cols, long e);
long trapped_vals(const vector<long>& v, int rows, int cols);
