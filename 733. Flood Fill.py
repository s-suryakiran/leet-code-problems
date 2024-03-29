class Solution:
    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, cur):
        if(sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0])):
            return;
        if(cur != image[sr][sc]):
            return;
        image[sr][sc] = color;
        self.fill(image, sr-1, sc, color, cur);
        self.fill(image, sr+1, sc, color, cur);
        self.fill(image, sr, sc-1, color, cur);
        self.fill(image, sr, sc+1, color, cur);

        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: 
            return image;
        self.fill(image, sr, sc, color, image[sr][sc]);
        return image;
        
        
            
            
        