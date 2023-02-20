import benchmark
class color:
      PURPLE = '\033[95m'
      CYAN = '\033[96m'
      DARKCYAN = '\033[36m'
      BLUE = '\033[94m'
      GREEN = '\033[92m'
      YELLOW = '\033[93m'
      RED = '\033[91m'
      BOLD = '\033[1m'                                                               
      UNDERLINE = '\033[4m'
      END = '\033[0m'


print(color.GREEN + "Welcome to Benchmark v0.1!"+ color.END)
print(color.YELLOW + "Tests: Bubble sort (bblsrt)")
i = input(color.CYAN +"Enter a test ID: " + color.END)

amtarr = int(input(color.CYAN+"How many arrays?\n"+color.END))
lenarr = int(input(color.CYAN +"How many numbers in each arrays?\n"+ color.END))

benchmark.bubblesort(amtarr,lenarr,False,False,True)