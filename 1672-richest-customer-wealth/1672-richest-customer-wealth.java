class Solution {
    public int maximumWealth(int[][] accounts) {
        int res = 0;
        
        for(int[] customer : accounts) {
            int sum = 0;
            for ( int account : customer) {
                sum += account;
            }
            res = Math.max(res,sum);
        }
    
        return res;
    }
}
