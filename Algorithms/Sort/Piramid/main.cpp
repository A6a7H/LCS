#include <iostream>
#
void siftdown(int* arr, int& size, int i){
    int count = (size>>1)-1;
    while (i <= count){
        int left = (i << 1) + 1;
        int right = (i << 1) + 2;
        int j = left;
        if (right < size and arr[right] > arr[left])
            j = right;
        if (arr[i] >= arr[j])
            break;
        int a = arr[i];
        arr[i] = arr[j];
        arr[j] = a;
        i = j;
    }
}

void sort(int* arr, int& size) {

    for (int i = (size >> 1) - 1; i >= 0; --i) {
        siftdown(arr, size, i);
    }

    for (int i = size - 1; i >= 0; i--) {
        std::swap(arr[0], arr[i]);
        siftdown(arr, i, 0);
    }
}


int main() {
    int* arr = new int[3]{11,33,22};
    int a = 3;
    sort(arr,a);
    for (int i =0;i<3;i++)
        std::cout << arr[i];
    return 0;
}