def main():
    number_of_ingredients = int(input())
    quantity_of_ingredients_required = list(map(int,input().split()))
    quantity_of_ingredients_present = list(map(int, input().split()))
    minimum_no_of_ppfgirls = quantity_of_ingredients_present[0]//quantity_of_ingredients_required[0]
    for i in range(1, number_of_ingredients):
        minimum_no_of_ppfgirls = min(minimum_no_of_ppfgirls, quantity_of_ingredients_present[i]//quantity_of_ingredients_required[i])
    print(minimum_no_of_ppfgirls)


main()
