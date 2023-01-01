class Solution {
    public int maximumWealth(int[][] accounts) {
        int sum = 0;
        int a[] = new int[accounts.length];
        for(int i = 0; i < accounts.length; i++){
            for(int j = 0; j < accounts[i].length; j++){
                sum += accounts[i][j];
                a[i] = sum;
            }
            sum = 0;
        }
        int max = 0;
        int min = 0;
        for(int k = 0; k < a.length; k++) {
            if(max < a[k]){
                max = a[k];
            }
            else if(max > a[k]) {
                min = a[k];
            }
        }
        return max;
    }
}
