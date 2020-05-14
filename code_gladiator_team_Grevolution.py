def main():
    test_cases = int(input())
    for i in range(test_cases):
        number_of_players = int(input())

        grev_power = sorted(list(map(int, input().split())))
        opp_power = sorted(list(map(int, input().split())))
        max_win = 0
        grev_power_counter, opp_power_counter = 0, 0
        while grev_power_counter < number_of_players:
            if grev_power[grev_power_counter] > opp_power[opp_power_counter]:
                max_win += 1
                grev_power_counter += 1
                opp_power_counter += 1
            else:
                grev_power_counter += 1
        print(max_win)

main()
