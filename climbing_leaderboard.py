def climbingLeaderboard(scores, alice):
    leaderboard = scores
    alice = alice[:5]
    max_index = len(leaderboard)
    ranks = []
    rank = 1
    flag = True
    for i in range(0, max_index):
        # print(leaderboard[i])
        if i + 1 == max_index:
            if alice[0] < leaderboard[i]:
                rank += 1
                flag = False
            else:
                flag = False
                break
        elif leaderboard[i] != leaderboard[i + 1]:
            if alice[0] < leaderboard[i]:
                rank += 1
                flag = False
            else:
                flag = False
                break
    if not flag:
        ranks.append(rank)
        max_index = i

    for j in alice[1:]:
        flag = True
        for i in range(max_index, -1, -1):
            if i-1 == -1:
                if j >= leaderboard[i]:
                    flag = False
                else:
                    rank -= 1
                    flag = False
                    break
            elif leaderboard[i] != leaderboard[i-1]:
                if leaderboard[i-1] > j >= leaderboard[i]:
                    flag = False
                else:
                    rank -= 1
                    flag = False
                    max_index = i -1
                    break
        if not flag:
            print(j, rank)
            ranks.append(rank)
    return ranks

if __name__ == "__main__":
    scores_count = int(input())
    scores = list(map(int, input().rstrip().split()))
    alice_count = int(input())
    alice = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(scores, alice)
    print(result)
