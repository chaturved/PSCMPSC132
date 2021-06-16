from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.player_list=[]; #Player objects
        self.dealer=Dealer();
        for name in player_names:
            self.player_list.append(Player(name,self.dealer));
        return None

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        res="";
        f=0;
        temp=[] #For natural blackjack, stores index value of player
        for rounds in range(1,num_rounds+1):
            f=0;
            temp=[];
            self.dealer.shuffle_deck();
            for i in range(0,2):
                for j in range(0,len(self.player_list)):
                    self.dealer.signal_hit(self.player_list[j]);
                self.dealer.hand.append(self.dealer.deck.draw());

            for i in range(0,len(self.player_list)):
                if(self.player_list[i].card_sum==21):
                    if(sum(self.dealer.hand)!=21):
                        self.player_list[i].record_win();
                        temp.append(i);
                        #exit();
                elif(sum(self.dealer.hand)==21):
                    f=1;
                    if(self.player_list[i].card_sum==21):
                        self.player_list[i].record_tie();
                        temp.append(i);
                        
            if(f==1):
                for j in range(0,len(self.player_list)):
                    if j not in temp:
                        self.player_list[j].record_loss();
                    res=self.stats(res,rounds);
                    
                continue;
                        

            for i in range(0,len(self.player_list)):
                self.player_list[i].play_round();
            self.dealer.play_round();
            

            for i in range(0,len(self.player_list)):
                if i in temp:
                    continue;
                
                if(sum(self.dealer.hand)>21):
                    if(self.player_list[i].card_sum<=21):
                        self.player_list[i].record_win();
                    else:
                        self.player_list[i].record_loss();
                        
                else:
                    if(self.player_list[i].card_sum<=21):
                        if(self.player_list[i].card_sum>sum(self.dealer.hand)):
                            self.player_list[i].record_win();
                        elif(self.player_list[i].card_sum==sum(self.dealer.hand)):
                            self.player_list[i].record_tie();
                        else:
                            self.player_list[i].record_loss();
                    else:
                        self.player_list[i].record_loss();
                        
            res=self.stats(res,rounds);
        return res[0:len(res)-1];
                           
            
            
    def stats(self,res,rounds):
        res=res+"Round {}\n".format(rounds)+str(self.dealer)+"\n";
        for i in range(0,len(self.player_list)):
            res=res+str(self.player_list[i])+"\n";
                
        for i in range(0,len(self.player_list)):
            self.player_list[i].discard_hand();
        self.dealer.hand=[];

        return res;
                           
            

            
        

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for i in range(0,len(self.player_list)):
            self.player_list[i].discard_hand();
            self.player_list[i].reset_stats();
        
        self.dealer.hand=[];   
        
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
