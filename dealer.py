from player import Player
from card_deck import CardDeck


class Dealer(Player):

    def __init__(self):
        self.name="Dealer";
        self.deck=CardDeck();
        super().__init__(self.name,self);
        self.hand=[];
        return None

    def shuffle_deck(self):
        """
        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> str(dealer.deck)[0:20]
        '10 8 10 6 8 9 3 10 2'
        """
        self.deck.shuffle();
        
        return None

    def signal_hit(self, player):
        """
        A method called by players when they want to hit
        Player objects should pass their `self` references to this method
        Should deal one card to the player that signalled a hit

        These doctests will not run properly if the `deal_to` method 
        in the `Player` class is not properly implemented

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> player = Player(None, None)
        >>> dealer.signal_hit(player)
        >>> player.hand
        [10]
        """
        player.deal_to(self.deck.draw());
        return None

    def play_round(self):
        """
        A dealer should hit if his hand totals to 16 or less

        >>> import random; random.seed(1)
        >>> dealer = Dealer()
        >>> dealer.shuffle_deck()
        >>> dealer.play_round()
        >>> dealer.hand
        [10, 8]
        """
        if(sum(self.hand)<17):
            self.hand.append(self.deck.draw());
            return self.play_round();
        elif(sum(self.hand)>=17):
            return None;


if __name__ == "__main__":
    import doctest
    doctest.testmod()
