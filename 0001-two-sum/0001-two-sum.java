class Solution {
    public static int[] twoSum(int[] nums, int target) {
        //It is allowed to use Wrapper class there, not primitive type 'int'
        Map<Integer, Integer> map = new HashMap<>();
        int complement;
        for(int i = 0; i < nums.length; i++) {
            complement = target - nums[i];
            if(map.containsKey(complement)) {
                //.get() : Returns the 'value' to which the specified key is mapped
                return new int[] {i, map.get(complement)};
            }
            map.put(nums[i], i);
        }
        return nums;
    }
}