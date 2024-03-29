public class Solution {
    public boolean isAnagram(String s, String t) {
        if(s == null || t == null) {
            return false;
        }
        char[] arr1 = s.toCharArray();
        char[] arr2 = t.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int length = arr1.length > arr2.length ? arr1.length : arr2.length;
        for (int i = 0; i < length; i++) {
                        if(length > (arr1.length)) {
                return false;
            }
            if(length > (arr2.length)) {
                return false;
            }
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }
}

//Runtime: 3 ms, faster than 89.31% of Java online submissions for Valid Anagram.
//Memory Usage: 42.9 MB, less than 40.03% of Java online submissions for Valid Anagram.
