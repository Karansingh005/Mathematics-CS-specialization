#Program that for any integer amount in the range from 24 to 1000 returns a list consisting of numbers 5 and 7 only, such that their sum is equal to amount.
def change(amount):
  if amount == 24:
    return [5, 5, 7, 7]
  elif amount == 25:
    return [5,5,5,5,5]
  elif amount == 26:
    return [5,7,7,7]
  elif amount == 27:
    return [5,5,5,5,7]
  elif amount == 28:
    return [7,7,7,7]
  else: 
    coins = change(amount - 5)
    coins.append(5)
    return coins

if __name__ == "__main__":

    n = int(input())
    print(change(n))
