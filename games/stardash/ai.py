# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI
import math

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here

# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Stardash. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.stardash.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.stardash.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "FlatEarthSquad" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn

        #assign target variable
        target = self._player.home_base
        self._toMine = None

        #Parse Bodies
        bodies = self._game.bodies
        
        for _ in bodies:
            if _.body_type == "asteroid":
                if _.material_type == 'legendarium':
                    if self._toMine == None:
                        self._toMine = _
                    else:
                        prior = self._toMine
                        
                    if self._toMine != None:
                        dist = self._player.home_base.x
                        if dist - _.x < dist - self._toMine.x:
                            if dist - _.y < dist - self._toMine.y:
                                self._toMine = _
                            else:
                                self._toMine = prior
                            

        #Parse Units
        #Can optimize movement with range
        units = self._game.units
        
        for _ in units:
            if _.owner == self._player:
                if _.job.title == "miner":
                    if _.genarium == 0 and _.rarium == 0 and _.legendarium == 0 and _.mythicite == 0:
                        target = self._toMine
                        if self._toMine.amount == 0:
                            self._toMine = None
                            target = self._player.home_base

                    if target.body_type == "planet":
                        if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                            if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                                print("I have reached the Base, proximety depositing now.")
                            else:
                                _.dash(target.x, target.y)
                                print("Dashing back to Base X:" + str(target.x) + ",Y:" + str(target.y))
                                print("I am currently at X:" + str(_.x) + ", Y:" + str(_.y))
                         
                    movX = (target.x - _.x)
                        
                    movY = (target.y - _.y)

                    if math.fabs(movX) > _.moves:
                        movX = math.copysign(_.moves, movX)
                        
                    if _.safe(_.x + movX, _.y) == False:
                        _.dash(target.x, target.y)
                        print("Sun encountered, dashing.")
                    elif movX != 0.0:    
                        _.move(_.x + movX, _.y)
                        print("Moving to X:" + str(_.x + movX))

                    if math.fabs(movY) > _.moves:
                        movY = math.copysign(_.moves, movY)

                    if _.safe(_.x, _.y + movY) == False:
                        _.dash(target.x, target.y)
                        print("Sun encountered, dashing.")
                    elif movY != 0.0: 
                        _.move(_.x, _.y + movY)
                        print("Moving to Y:" + str(_.y + movY))
                     
                    if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                        if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                            if target.body_type == "asteroid":
                                _.mine(target)
                                print("Mining")

                    if _.genarium + _.rarium + _.legendarium + _.mythicite >= _.job.carry_limit:
                        target = self._player.home_base
        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
