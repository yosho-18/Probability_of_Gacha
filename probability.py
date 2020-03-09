from matplotlib import pyplot as plt

def hit(N): # 1 / N の確率で当たる事象をN回行ったときに1回以上当たる確率
    return 1 - (1 - 1 / N) ** N

start = 2
end = 500
probability = [hit(i) for i in range(start, end + 1)]
number = [i for i in range(start, end + 1)]

def graph(probability):
    plt.rcParams["font.size"] = 18
    plt.figure()
    plt.plot(number, probability)
    plt.xlabel('number')
    plt.ylabel('probability')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("probability" + ".png")
    plt.savefig("probability" + ".eps")
    plt.show()

graph(probability)
