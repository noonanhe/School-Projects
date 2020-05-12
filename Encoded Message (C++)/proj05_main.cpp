#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using std::string;
using std::cin; using std::cout; using std::endl; 
using std::getline;
using std:: pow; using std::boolalpha;
using std::vector;

#include "proj05_functions.h"

int main (){
  cout << boolalpha;
  int testnum;
  cin >> testnum;

  switch (testnum){

  case 1: {
    string s;
    cin.ignore(1000, '\n');
    getline(cin,s);
    cout << lower_case(s)  <<endl;
    break;
  }
    
  case 2: {
    char c;
    cin >> c;
    cout << to_binary(c) <<endl;
    break;
  }

  case 3:{
    string n;
    cin >> n;
    cout << from_binary(n) << endl;
    break;
  }

  case 4: {
    cin.ignore(1000, '\n');
    string plain, secret;
    getline(cin, plain);;
    getline(cin,secret);
    cout << check_message(plain, secret) << endl;
    break;
  }

  case 5: {
    cin.ignore(1000, '\n');
    string plain, secret;
    getline(cin, plain);
    getline(cin, secret);
    cout << encode(plain, secret) << endl;
    break;
  }

  case 6: {
    cin.ignore(1000, '\n');
    string encoded;
    getline(cin, encoded);
    cout << decode(encoded) << endl;
    break;
  }    

  }// of switch
} // of main
