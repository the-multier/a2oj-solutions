int addDigitsHelper(int num) {
    int sum = 0;
    while (num > 0) {
        int current = num % 10;
        sum += current;
        num /= 10;
    }
    return sum;
}

int addDigits(int num) {
    while (num > 9) {
        num = addDigitsHelper(num);    
    }
    return num;
}
