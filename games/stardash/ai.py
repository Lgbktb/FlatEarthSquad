# This is where you build your AI for the Stardash game.

import math
import copy
from joueur.base_ai import BaseAI
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
        return "TheGlobalists" # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """ 
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        
        self._ourMiners = []
        self._enemyMiners = []
        self._none = [] #Debug purposes, should be empty
        self._genarium = []
        self._rarium = []
        self._legendarium = []
        self._mythicite = []
        self._theSun = self._game.bodies[2]

        #Find our Miners
        for i in self._game.units:
            if i.owner == self._player:
                self._ourMiners.append(i)
            else:
                self._enemyMiners.append(i)
        #print(str(self._ourMiners))

        #Identify Celestial Bodies
        for i in self._game.bodies:
            if i.body_type == 'asteroid':
                if i.material_type == "none":
                    self._none.append(i)
                elif i.material_type == "genarium":
                    self._genarium.append(i)
                elif i.material_type == "rarium":
                    self._rarium.append(i)
                elif i.material_type == "legendarium":
                    self._legendarium.append(i);
                elif i.material_type == "mythicite":
                    self._mythicite.append(i);
                else:
                    print("Unknown Planet Type")
        #print("none: " + str(self._none))
        #print("generium: " + str(self._genarium))
        #print("rarium: " + str(self._rarium))
        #print("legendarium: " + str(self._legendarium))
        #print("mythicite: " + str(self._mythicite))

        
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
        print("Turn start")
        potentialTargets = copy.deepcopy(self._legendarium) # All potential Targets for each of ourMiners
        lockedTargets = [] # Locked target for each Miner, corresponding to each miner (lockedTargets[0] goes with _ourMiners[0])
        for i in self._ourMiners:
            
            # Idendify closest Legendarium
            if(potentialTargets): 
                closestLegendarium = potentialTargets[0]
                for j in potentialTargets:
                    if (self.distance(j.x, i.x, j.y, i.y) < self.distance(closestLegendarium.x, i.x, closestLegendarium.y, i.y)): 
                        closestLegendarium = j
                # Set as Locked Target
                lockedTargets.append(closestLegendarium)
                # Remove chosen target from pool of potential targets
                potentialTargets.remove(closestLegendarium)
                
                if(i.job.carry_limit == i.legendarium):
                    print("Returning to base")
                    #Move Toward Home base
                    self.sendHome(i)
                    #i.dash(self._player.home_base.x, self._player.home_base.y)

                # Attempt to mine
                if(i.mine(closestLegendarium)):
                    print("MINING SUCCESSS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                else:
                    #Attempt to Dash to Location
                    i.dash(closestLegendarium.x, closestLegendarium.y)
            else:
                print("No Potential Targets :(")
        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    def distance(self, x1, x2, y1, y2):
        return math.sqrt((x2 - x1 )**2 + (y2 - y1)**2)
    def moveTo(self, obj, x, y):
        #Moves obj towars coordinates    x, y
        #Doesn't Work at all
        trix = abs(x-obj.x)
        triy = abs(y-obj.y)
        
        dist = self.distance(obj.x, trix, obj.y, triy)
        ix = obj.moves * trix / dist
        iy = obj.moves * triy / dist
        print("Dist: " + str(dist))
        print("Movement: " + str(obj.moves))
        print("Ix: " + str(ix) + ": IY: " + str(iy) )
        obj.move(obj.x+ix, obj.y+iy)
    
    def sendHome(self, obj):
        #Moves object toward home_base
        #Doesn't work at all
        print("SEnding em on home")
        homeX = self.player.home_base.x
        homeY = self.player.home_base.y
        dist = self.distance(homeX, obj.x, homeY, obj.y)
        myMoves = obj.moves / 2 #TEsting Only

        ix = myMoves*(homeX-obj.x)/dist
        iy = myMoves*(homeY-obj.y)/dist
        print("Ix: " + str(ix) + ": IY: " + str(iy) )
        obj.move(obj.x+ix, obj.y+iy)
    # <<-- /Creer-Merge: functions -->>
