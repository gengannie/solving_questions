def main(words, order):
    order_m = {}
    for count, i in enumerate(order):
        order_m [i] = count
    prev_str = words [0]
    words = words [1:]
    for word in words:
        for j in range(0, len(prev_str)):
            p_i = prev_str [j]
            p_i = order_m[p_i]
            t_i = order_m[word [j]] if j < len(word) else -1
            if (t_i < p_i):
                return False
            elif (t_i == p_i):
                continue
            elif (t_i > p_i):
                break
        prev_str = word
    return True

if __name__ == "__main__":
    print(main(["h", "hallothere", "hejhduw"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(main(["aa","a"], "abcdefghijklmnopqrstuvwxyz"))