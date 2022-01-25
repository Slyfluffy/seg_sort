# 1. Name:
#      Journey Curtis
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      Sorts the program by segregating it into smaller parts.
# 4. What was the hardest part? Be as specific as possible.
#      It was pretty easy this time. I guess I could say
#      taking the time to program the sort.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours

#####################################
# SEG_SORT :: GET_LIST
# INPUTS   :: NONE
# OUTPUTS  :: LIST
# Returns a list selected by the user
#####################################
def get_list():
   list = []
   
   # We could  turn get_list into a file reading function
   # or a manual input for lists. Since we are only testing
   # the algorithm I went with hard-coded options instead.

   print("OPTIONS:\n1: empty\n2: 1 item list\n3: 2 item list")
   print("4: pre-sorted list\n5: duplicate entry list\n6: reverse sorted")
   print("7: Multi-number out of order\n8: Bro. Helfrich's example")
   
   option = int(input("Please enter a list option: "))

   # We could change these lists to use words or a combo of numbers/letters
   if option == 2: # 1 item
      list.append(5)
   elif option == 3: # 1 item
      list = [2, 1]
   elif option == 4: # pre-sorted
      list = [1, 2, 3, 4, 5]
   elif option == 5: # duplicates
      list = [15, 5, 12, 20, 2, 2, 4, 5]
   elif option == 6: # reverse sorted
      list = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
   elif option == 7: # many numbers
      list = [31, 72, 10, 32, 18, 95, 25, 50]
   elif option == 8: # Bro. Helfrich's example
      list = [1,5,4,8,3,1,10,2,4,8,19,3,2,1]

   return list

######################################
# SEG_LIST :: SORT
# INPUTS   :: ARRAY
# OUTPUTS  :: ARRAY, I_START, I_END
# Wrapper function for sort_recursive.
# Sends all the data needed to
# sort_recursive
######################################
def sort(array):
   sort_recursive(array, 0, len(array) - 1)

#####################################
# SEG_LIST :: SORT_RECURSIVE
# INPUTS   :: ARRAY, I_START, I_END
# OUTPUTS  :: ARRAY
# 
#####################################
def sort_recursive(array, i_start, i_end):
   if i_end - i_start < 1 or i_end < 0:
      return

   i_pivot = segregate(array, i_start, i_end)

   sort_recursive(array, i_start, i_pivot - 1)
   sort_recursive(array, i_pivot + 1, i_end)

#####################################
# SEG_LIST :: SEGREGATE
# INPUTS   :: ARRAY, I_START, I_END
# OUTPUTS  :: ARRAY
# 
#####################################
def segregate(array, i_begin, i_end):
   if i_begin == i_end:
      return i_begin

   i_pivot = (i_begin + i_end) // 2
   i_up = i_begin
   i_down = i_end

   while i_up < i_down:
      while i_up < i_down and array[i_up] < array[i_pivot]:
         i_up += 1
      while i_up < i_down and array[i_down] >= array[i_pivot]:
         i_down -= 1
      
      if i_up < i_down:
         if i_down == i_pivot:
            i_pivot = i_up
         elif i_up == i_pivot:
            i_pivot = i_down
         temp = array[i_up]
         array[i_up] = array[i_down]
         array[i_down] = temp

   temp = array[i_up]
   array[i_up] = array[i_pivot]
   array[i_pivot] = temp

   return i_up

#################################
# SEG_SORT :: DISPLAY_LIST
# INPUTS   :: LIST
# OUTPUTS  :: NONE
# Displays a message depending if 
# the list is sorted or not
#################################
def display_list(list):
   print(list)

###########################
# SUB_LIST :: MAIN
# INPUTS   :: NONE
# OUTPUTS  :: NONE
# Runs the sub_list program
###########################
def main():
   list = get_list()
   display_list(list)
   sort(list)
   display_list(list)

main()