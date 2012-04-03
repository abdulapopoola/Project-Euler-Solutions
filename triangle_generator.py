def triangle(n):
    tri = [[1],[1,1]]
    if n <= len(tri):
        return tri[:n]
    else:
        while (len(tri)<n):
            i = len(tri)
            tmp = [0] *(i+1)
            tmp[0] = tri[-1][0]
            tmp[-1] = tri[-1][-1]
            for j in range(i-1):
                tmp[j+1] = tri[-1][j] + tri[-1][j+1]
            tri.append(tmp)
        return tri


print triangle(6)
