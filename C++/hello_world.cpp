#include <iostream>
using namespace std;

int main() {
  double sales = 95000;
  auto state_tax = (sales) * (0.04);
  double county_tax = (sales) * (0.02);
  cout << sales << endl << state_tax << endl << county_tax;

  return 0;
}