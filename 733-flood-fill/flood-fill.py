class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        srq, scq = deque(), deque()
        srq.append(sr)
        scq.append(sc)
        startColor = image[sr][sc]
        while srq and scq:
            r = srq.popleft()
            c = scq.popleft()

            if image[r][c]!=color:
                image[r][c]=color
                if r-1>=0:
                    if image[r-1][c]==startColor:
                        srq.append(r-1)
                        scq.append(c)
                if r+1<m:
                    if image[r+1][c]==startColor:
                        srq.append(r+1)
                        scq.append(c)
                if c-1>=0:
                    if image[r][c-1]==startColor:
                        srq.append(r)
                        scq.append(c-1)
                if c+1<n:
                    if image[r][c+1]==startColor:
                        srq.append(r)
                        scq.append(c+1)
        return image

           


  


'''
srq = [0, 1]
scq = [1, 0]
Input: image = [[2,2,2],
                [2,2,0],   
                [2,0,1]], 
                
                sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

'''