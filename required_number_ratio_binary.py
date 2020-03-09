from matplotlib import pyplot as plt

start = 2
end = 500
number = [i for i in range(start, end + 1)]

# 95%
def hit_theta(N, K):  # 1 / N の確率で当たる事象をK回行ったときに1回以上当たる確率
    return 1 - (1 - 1 / N) ** K

def graph_theta(theta, required_number_ratio):  # グラフ
    plt.rcParams["font.size"] = 18
    plt.figure()
    plt.plot(number, required_number_ratio)
    plt.xlabel('number')
    plt.ylabel('need_count_rate')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("required_number_ratio" + str(theta) + ".png")
    plt.savefig("required_number_ratio" + str(theta) + ".eps")
    plt.show()

K = 0
theta = 0.95
required_number_ratio = []
for N in range(start, end + 1):
    while True:
        if hit_theta(N, K) > theta:
            #print("N", N, "K", K)
            #print(K / N)
            required_number_ratio.append(K / N)
            break
        K += 1
graph_theta(theta, required_number_ratio)

required_number_ratio_binary = []

# 条件を満たす最小値（ng,ok）
def binary_search():
    ng = -1 #「index = 0」が条件を満たすこともあるので、初期値は -1
    ok = 10 ** 15 #「index = a.size()-1」が条件を満たさないこともあるので、初期値は a.size()

    #ok と ng のどちらが大きいかわからないことを考慮
    while abs(ok - ng) > 1:
        K = (ok + ng) // 2
        if hit_theta(N, K) > theta:
            ok = K
        else:
            ng = K
    return ok

for N in range(start, end + 1):
    K = binary_search()
    required_number_ratio_binary.append(K / N)

graph_theta(theta, required_number_ratio_binary)
print(required_number_ratio == required_number_ratio_binary)

# 99%
K = 0
theta = 0.99
required_number_ratio = []
for N in range(start, end + 1):
    while True:
        if hit_theta(N, K) > theta:
            #print("N", N, "K", K)
            #print(K / N)
            required_number_ratio.append(K / N)
            break
        K += 1

graph_theta(theta, required_number_ratio)