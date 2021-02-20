
class coin_change_sol:

    def __init__(self,coins=[1,2,5],sol = "Dict"):

        self.memo = {}
        self.wallet = coins
        self.sol = sol

    
    def find_mini_coin_required(self,money):


        if money == 0:

            return 0

        if money<0:

            return -1
        

        if self.sol == "Dict":

            if money in self.memo:

                return self.memo[money]

            best_Amt = money

            for i in self.wallet:

                subproblem = self.find_mini_coin_required(money - i)

                if subproblem != -1:

                    best_Amt = min( best_Amt,1+subproblem)

        

            if best_Amt != money:

                self.memo[money] = best_Amt

                return best_Amt

            else:

                return -1


        elif self.sol == "List":

            min_sol_list = [money]*money

            for i in range(len(min_sol_list)):

                for coin in self.wallet:

                    if (i+1-coin)>0:
                        
                        min_sol_list[i] = min(min_sol_list[i],1+min_sol_list[i-coin])

                    elif (i+1-coin)==0:

                        min_sol_list[i] = 1


            if min_sol_list[money-1] == money:

                return -1

            else:

                return min_sol_list[money-1]
            




test_A = coin_change_sol()

test_B = coin_change_sol(sol="List")





















            
    
