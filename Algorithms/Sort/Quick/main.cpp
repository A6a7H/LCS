#include <iostream>

void merge(int* arr, int first, int second, int end)
{
    int cnt1 = 0;
    int cnt2 = 0;
    int* buff = new int[end-first];
    while (first + cnt1 < second and second + cnt2 < end){
        if (arr[first + cnt1] < arr[second + cnt2]){
            buff[cnt1 + cnt2] = arr[first + cnt1];
            cnt1++;
        }
        else{
            buff[cnt1 + cnt2] = arr[second + cnt2];
            cnt2++;
        }
    }
    while (first + cnt1 < second){
        buff[cnt1 + cnt2] = arr[first + cnt1];
        cnt1++;
    }
    while (second + cnt2 < end){
        buff[cnt1 + cnt2] = arr[second + cnt2];
        cnt2++;
    }
    for (int i =0; i < end-first; i++){
        arr[first + i] = buff[i];
    }
    delete[] buff;
}

void divide_and_merge(int *arr, int left, int right)
{
    if (left + 1 >= right)
        return;
    int mid = (left + right)/2;
    divide_and_merge(arr, left, mid);
    divide_and_merge(arr, mid, right);
    merge(arr,left, mid, right);
}

void sort(int *arr, int length)
{
    int l = 0;
    int r = length;
    divide_and_merge(arr,l,r);
}

int main() {
    int* ms = new int[3]{33, 22, 11};
    sort(ms,3);
    for (int i = 0; i < 3; i++){
        std:: cout << ms[i] << " ";
    }
}