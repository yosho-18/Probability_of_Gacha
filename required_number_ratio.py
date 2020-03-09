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
    plt.ylabel('required_number_ratio')
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


# 99%
K = 0
theta = 0.99
required_number_ratio = []
for N in range(start, end + 1):
    while True:
        if hit_theta(N, K) > theta:
            print("N", N, "K", K)
            print(K / N)
            required_number_ratio.append(K / N)
            break
        K += 1

graph_theta(theta, required_number_ratio)