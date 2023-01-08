class Solution {
    public List<String> fizzBuzz(int n) {
        String[] array = new String[n];
        for(int i = 0; i < n; i++) {
            array[i] = (i+1)+"";
            if (i >= 2 && i%3 == 2) {
                array[i] = "Fizz";
            }
            if (i >= 4 && i%5 == 4) {
                array[i] = "Buzz";
            }
            if ((i >= 2 && i%3 == 2) && (i >= 4 && i%5 == 4)) {
                array[i] = "FizzBuzz";
            }
        }
        return Arrays.asList(array);
    }
}
