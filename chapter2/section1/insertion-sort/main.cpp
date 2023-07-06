//
// Created by cmtheit on 23-7-5.
//

#include <iostream>
#include <vector>
#include <cassert>

using namespace std;
void sort(vector<int> & v) {
    // 初始化：循环之前，v[1..i - 1] 为有序的
    for (int i = 1; i < v.size(); ++i) {
        int p = i - 1;
        int key = v[i];
        // 初始化：循环之前，v[p] ~ v[i] 之间的所有元素都比 v[i] 大 ( p == i - 1 )
        while (v[p] > key && p >= 0) {
            v[p + 1] = v[p];
            p--;
            // 保持：循环之后，v[p] ~ v[i] 之间的所有元素都比 v[i] 大
        }
        // 终止： v[p] ~ v[i] 之间的所有元素都比 v[i] 大，v[p] 不比 v[i] 大
        v[p + 1] = key;
        // 保持：循环之后，v[1..i] 为有序的
    }
    // 终止：v[1..v.length] 为有序的
}

bool ordered(vector<int> & v) {
    for (int i = 0; i < v.size() - 1; ++i) {
        if (v[i + 1] < v[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<int> a {9, 4, 5, 1, 43, 0, 8, -9};
    sort(a);
    assert(ordered(a));
    cout << "It is ordered." << endl;
}