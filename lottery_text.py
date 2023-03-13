# -----------------------------------------------------------------------------
#
# lottery_text.py
#
# Created and Version: 03/13/23 0.1
#
# remarks: Tries to predict the next drawing of the South Korean Lotterty
#          6/45 LOTTO
#---------------------------------------------------------------------------

#Need pandas and collections to help read the Excel file and put it in lists 
import pandas as pd
from collections import Counter

#Create empty list to hole numbers
numbers_to_play = []
bonus_number_to_play = []

#Read sheet 1 in the Excel file return list of regular numbers
def read_xlsx_and_convert_regular_numbers():
    filedata = pd.read_excel("numbers.xlsx", "Sheet1")

    list_of_rows = filedata.values.tolist()

    list_of_numbers = []

    for row in list_of_rows:
        for num in row:
            list_of_numbers.append(num)

    return list_of_numbers
#Read sheet2 in the Excel file and return the bonus numbers 
def read_xlsx_and_convert_bonus_numbers():
    filedata = pd.read_excel("numbers.xlsx", "Sheet2")

    list_of_rows = filedata.values.tolist()
    list_of_bonus_numbers = []

    for row in list_of_rows:
        for num in row:
            list_of_bonus_numbers.append(num)

    return list_of_bonus_numbers

#Run Prediction on regular numbers 1-45
def predict_future_numbers(past_numbers):
  counter = Counter(past_numbers)
  most_common = counter.most_common(6)

  for number, count in most_common:
      number = int(number)
      numbers_to_play.append(number)
  numbers_to_play.sort()

  print('Numbers to Play: ', numbers_to_play)

#Run prediction on bonum number 1-45
def predict_future_bonus_number(past_bonus_numbers):
    counter = Counter(past_bonus_numbers)
    most_common = counter.most_common(1)

    for number, count in most_common:
        number = int(number)
        bonus_number_to_play.append(number)
    print("Bonus ball to play: ", bonus_number_to_play) 

#Print out the results to the console.
past_winning_numbers = read_xlsx_and_convert_bonus_numbers()
predict_future_numbers(past_winning_numbers)

past_bonus_number = read_xlsx_and_convert_bonus_numbers()
predict_future_bonus_number(past_bonus_number)
        
#END