import numpy as np

e = 0.00001

A_1 = np.array([[1,0,0],[0,5,-1],[0,3,0]])
A_2 = np.array([[1,0,0],[0,0,-1],[0,3,0]])

def calc(A,x):
    i = 0
    x = x/np.linalg.norm(x) #xのノルムは1で固定
    while(i < 10000): #10000回繰り返すことにする
        new_x = np.dot(A,x) #ここで、停止条件を「xの更新が十分小さい」と読み替える
        if np.linalg.norm(x * np.linalg.norm(new_x) - new_x) < e:
            print("eigenvalue:", np.linalg.norm(new_x))
            print("steps:",i)
            return
        x = new_x / np.linalg.norm(new_x)
        i += 1
    print("No eigenvalue found.")
    return

x = np.array([[1],[1],[1]])

#実行部分
print("Case A_1")
calc(A_1,x)
print("Case A_2")
calc(A_2,x)
