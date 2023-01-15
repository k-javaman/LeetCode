class Solution {
    public int trap(int[] height) {
		
		// less than 3 bars can not trap any water
		if(height.length < 3)
			return 0;
		
		// create arrays for the max left and right values
		int[] leftMax = new int[height.length];
		int[] rightMax = new int[height.length];
		
		// calculating the left max values (from left to right)
		leftMax[0] = 0;
		
		for(int i=1;i<leftMax.length;++i)
			leftMax[i] = Math.max(leftMax[i-1], height[i-1]);
		
		// calculating the right max values (from right to left)
		rightMax[rightMax.length-1] = 0;
		
		for(int i=rightMax.length-2;i>=0;--i)
			rightMax[i] = Math.max(rightMax[i + 1], height[i+1]);
		
		// consider all the items in O(N) running time
		int trapped = 0;
		
		for(int i=1;i<height.length-1;i++)
			if(Math.min(leftMax[i], rightMax[i]) > height[i])
				trapped += Math.min(leftMax[i], rightMax[i]) - height[i];
		
		return trapped;
	}
}