# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI
import math
import copy

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
        self._ourMiners = []
        self._moneyMiners = []
        self._mythiciteMiners = []
        self._moneyTransporters = []
        self._mythiciteTransporters = []
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
                self._moneyMiners.append(i)
                """
                if self._mythiciteMiners: #One Mythicite Miner, 2 moneyMiners
                    self._moneyMiners.append(i)
                else: 
                    self._mythiciteMiners.append(i)
                """
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
        # Put your game logic here for runTurn
        print("Turn start: "+ str(self._game.current_turn))

        self.spawnUnits()

        # Parse Bodies
        target = None
        if self._moneyTransporters:
            target = self._moneyTransporters[0]
        else:
            target = self._player.home_base
        for i in self._moneyMiners:
            toMine = self.getTarget(i, self._legendarium)
            self.moveMiner(i, target, toMine)
        
        if self._mythiciteTransporters:
            target = self._mythiciteTransporters[0]
        else:
            target = self._player.home_base
        
        for i in self._mythiciteMiners:
            toMine = self.getTarget(i, self._mythicite)
            self.moveMiner(i, target, toMine)
        target = self._player.home_base
        for i in self._moneyTransporters:
            toMine = self.getTarget(i, self._legendarium)
            self.moveTransport(i, target, toMine)
        target = self._player.home_base
        for i in self._mythiciteTransporters:
            toMine = self.getTarget(i, self._mythicite)
            self.moveTransport(i, target, toMine)
        
        #Parse Units
        #Can optimize movement with range
        #units = self._game.units
        
        
        # for _ in units:
        #     # For every unit, does mining and movemetn
        #     if _.owner == self._player:
        #         if _.job.title == "miner":
                    # if _.genarium == 0 and _.rarium == 0 and _.legendarium == 0 and _.mythicite == 0:
                    #     target = self._toMine
                    #     if self._toMine.amount == 0:
                    #         self._toMine = None
                    #         target = self._player.home_base

                    # if target.body_type == "planet":
                    #     if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                    #         if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                    #             print("I have reached the Base, proximety depositing now.")
                    #         else:
                    #             _.dash(target.x, target.y)
                    #             print("Dashing back to Base X:" + str(target.x) + ",Y:" + str(target.y))
                    #             print("I am currently at X:" + str(_.x) + ", Y:" + str(_.y))
                         
                    # movX = (target.x - _.x)
                        
                    # movY = (target.y - _.y)

                    # if math.fabs(movX) > _.moves:
                    #     movX = math.copysign(_.moves, movX)
                        
                    # if _.safe(_.x + movX, _.y) == False:
                    #     _.dash(target.x, target.y)
                    #     print("Sun encountered, dashing.")
                    # elif movX != 0.0:    
                    #     _.move(_.x + movX, _.y)
                    #     print("Moving to X:" + str(_.x + movX))

                    # if math.fabs(movY) > _.moves:
                    #     movY = math.copysign(_.moves, movY)

                    # if _.safe(_.x, _.y + movY) == False:
                    #     _.dash(target.x, target.y)
                    #     print("Sun encountered, dashing.")
                    # elif movY != 0.0: 
                    #     _.move(_.x, _.y + movY)
                    #     print("Moving to Y:" + str(_.y + movY))
                     
                    # if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                    #     if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                    #         if target.body_type == "asteroid":
                    #             _.mine(target)
                    #             print("Mining")

                    # if _.genarium + _.rarium + _.legendarium + _.mythicite >= _.job.carry_limit:
                    #     target = self._player.home_base
        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    def spawnUnits(self):
        minMoneyMiners = 3
        maxMoneyMiners = 100
        minMythiciteMiners = 3
        maxMythiciteMiners = 10
        while self._player.money > 0:
            # MoneyMiners(Min)
            if self._player.money > 150 and len(self._moneyMiners) < minMoneyMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'miner')
                if self._game.units[len(self.game.units)-1].job.title == 'miner' :
                    self._moneyMiners.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the miner isn't the last unit")
            # MoneyTransport
            """elif self._player.money > 75 and not self._moneyTransporters and len(self._moneyMiners) > minMoneyMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'transport')
                if self._game.units[len(self.game.units)-1].job.title == 'transport' :
                    self._moneyTransporters.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the transport isn't the last unit")
            """
            # MythiciteMiners(Min)
            """
            elif self._player.money > 150 and len(self._mythiciteMiners) < minMythiciteMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'miner')
                if self._game.units[len(self.game.units)-1].job.title == 'miner' :
                    self._mythiciteMiners.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the miner isn't the last unit")
            # MythiciteTransport
            
            elif self._player.money > 75 and not self._mythiciteTransporters and len(self._mythiciteMiners) > minMythiciteMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'transport')
                if self._game.units[len(self.game.units)-1].job.title == 'transport' :
                    self._mythiciteTransporters.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the transport isn't the last unit")
            """
            #MaxMoneyMiners
            if self._player.money > 150 and len(self._moneyMiners) < maxMoneyMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'miner')
                if self._game.units[len(self.game.units)-1].job.title == 'miner' :
                    self._moneyMiners.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the miner isn't the last unit")
            """
            #MaxMythiciteMiners
            elif self._player.money > 150 and len(self._mythiciteMiners) < maxMythiciteMiners:
                self._player.home_base.spawn(self._player.home_base.x, self._player.home_base.y, 'miner')
                if self._game.units[len(self.game.units)-1].job.title == 'miner' :
                    self._mythiciteMiners.append(self._game.units[len(self.game.units)-1])
                else:
                    print("My Shit doesn't work, the miner isn't the last unit")
            """
            if False: #The enemy has spawned enemy-like units 
                pass #Create the Anti-Fuck Squad
            else:
                break

    
    def moveMiner(self, _, depotLoc, toMine):
        target = depotLoc
        if _.job.title == "miner":
                    print("Miner Turn")
                    print("Current Energy: " + str(_.energy))
                    
                    target = None
                    isDash = False
                    withinReach = False

                    if _.genarium + _.rarium + _.legendarium + _.mythicite == 0:
                        target = toMine
                    elif _.genarium + _.rarium + _.legendarium + _.mythicite >= _.job.carry_limit:
                        target = self._player.home_base
                    else:
                        target = self._player.home_base

                    if target != None:
                        print("Targeting:" + str(target.body_type) + " at X:" + str(target.x) + ", Y:" + str(target.y))
                        if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                            if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                                print("WithinReach of Target.")
                                withinReach = True

                        if withinReach == True:
                            if target.body_type == "asteroid":
                                _.mine(target)
                                print("Mining")
                                
                        dist = self.distance(_.x, _.y, target.x, target.y)

                        if _.acted == False:
                            if withinReach == False:
                                #Energy > DashesUsedForDistance + OneEnergyUnused
                                if _.energy > ((dist/50) + 1):
                                    #Distance/DashPerEnergy > 64 + (64/DashPerEnergy)
                                    if dist/50 > 1:
                                        if _.safe(target.x, target.y):
                                            print("Dashing from X:" + str(_.x) + ", Y:" + str(_.y))
                                            _.dash(target.x, target.y)
                                            isDash = True
                                            print("Dashing to X:" + str(target.x) + ", Y:" + str(target.y))
                                        else:
                                            print("Dashing from X:" + str(_.x) + ", Y:" + str(_.y))
                                            _.dash(target.x - 0.01, target.y - 0.01)
                                            isDash = True
                                            print("Dashing to X:" + str(target.x) + ", Y:" + str(target.y))

                            if isDash == False:
                                movX = (target.x - _.x)
                                    
                                movY = (target.y - _.y)

                                if math.fabs(movX) > _.moves:
                                    movX = math.copysign(_.moves, movX)
                                    
                                if _.safe(_.x + movX, _.y):
                                    _.move(_.x + movX, _.y)
                                    print("Moving to X:" + str(_.x + movX) + " at Rate:" + str(movX))
                                else:
                                    _.move(_.x + (movX - math.copysign(.01, movX)), _.y)
                                    print("Encountered Sun Rerouting.")
                                    print("Moving to X:" + str(_.x - (math.copysign(.01, movX))) + " at Rate:" + str(movX))

                                if math.fabs(movY) > _.moves:
                                    movY = math.copysign(_.moves, movY)
                                        
                                if _.safe(_.x, _.y + movY):
                                    _.move(_.x, _.y + movY)
                                    print("Moving to Y:" + str(_.y + movY) + " at Rate:" + str(movY))
                                else:
                                    _.move(_.x, _.y + (movY - math.copysign(.01, movY)))
                                    print("Encountered Sun Rerouting.")
                                    print("Moving to Y:" + str(_.y + (movY - math.copysign(.01, movY))) + " at Rate:" + str(movY))

                            if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
                                if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
                                    print("WithinReach of Target.")
                                    withinReach = True
                                    
                            if withinReach == True:
                                if target.body_type == "asteroid":
                                    _.mine(target)
                                    print("Mining")
                                if target.body_type == "planet":
                                    print("I have reached the Base. Proceding back to Mining.")
                    else:
                        print("No Target for Miner Selected")
        return target


        # if _.genarium == 0 and _.rarium == 0 and _.legendarium == 0 and _.mythicite == 0:
        #     target = toMine
        #     if toMine.amount == 0:
        #         toMine = None
        #         target = self._player.home_base 
        # if target.game_object_name == "Body":
        #     if target.body_type == "planet":
        #         if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
        #             if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
        #                 print("I have reached the Base, proximety depositing now.")
        #             else:
        #                 _.dash(target.x, target.y)
        #                 print("Dashing back to Base X:" + str(target.x) + ",Y:" + str(target.y))
        #                 print("I am currently at X:" + str(_.x) + ", Y:" + str(_.y))
        # if target.game_object_name == "Unit":
        #     if target.job.title == "transport":
        #         #target.job
        #         pass
        
        # movX = (target.x - _.x)
                       
        # movY = (target.y - _.y)

        # if math.fabs(movX) > _.moves:
        #     movX = math.copysign(_.moves, movX)
                    
        # if _.safe(_.x + movX, _.y) == False:
        #     _.dash(target.x, target.y)
        #     print("Sun encountered, dashing.")
        # elif movX != 0.0:    
        #     _.move(_.x + movX, _.y)
        #     #print("Moving to X:" + str(_.x + movX))

        # if math.fabs(movY) > _.moves:
        #     movY = math.copysign(_.moves, movY)

        # if _.safe(_.x, _.y + movY) == False:
        #     _.dash(target.x, target.y)
        #     print("Sun encountered, dashing.")
        # elif movY != 0.0: 
        #     _.move(_.x, _.y + movY)
        #     #print("Moving to Y:" + str(_.y + movY))
                     
        # if _.x + _.job.range >= target.x and _.x - _.job.range <= target.x:
        #     if _.y + _.job.range >= target.y and _.y - _.job.range <= target.y:
        #         if target.game_object_name == "Body":
        #             if target.body_type == "asteroid":
        #                 _.mine(target)
        #                 print("Mining")

        # if _.genarium + _.rarium + _.legendarium + _.mythicite >= _.job.carry_limit:
        #     target = self._player.home_base
        # return target


    def moveTransport(self, _, target, toMine):
        if _.genarium == 0 and _.rarium == 0 and _.legendarium == 0 and _.mythicite == 0:
            target = toMine
            if toMine.amount == 0:
                toMine = None
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
                    #_.mine(target)
                    #print("Mining")
                    pass

        if _.genarium + _.rarium + _.legendarium + _.mythicite >= _.job.carry_limit:
            target = self._player.home_base
        return target

    def getTarget(self, obj, listOfItems, ):
        """Returns the closest item in listofItems to obj
            example
            getTarget(self._player.home_base, self._game.bodies)
        """
        target = None;
        for _ in listOfItems:
            if target == None:
                target = _                   
                if target != None:
                    #dist = self._player.home_base.x
                    #Distance from the base to the astroid
                    newdist = self.distance(_.x, _.y, obj.x, obj.y)
                    olddist = self.distance(target.x, target.y, obj.x, obj.y)
                    if newdist < olddist:
                        target = _
        return target
    def distance(self, x1, y1, x2, y2):
        """ Returns the Euclidian distance between two points.

            Args:
                x1 (int): The x coordinate of the first point.
                y1 (int): The y coordinate of the first point.
                x2 (int): The x coordinate of the second point.
                y2 (int): The y coordinate of the second point.

            Returns:
                float: The distance between the two points.
        """
        return math.sqrt((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0)

    def find_dash(self, unit, x, y):
        """ This is an EXTREMELY basic pathfinding function to move your ship until it can dash to your target.
            You REALLY should improve this functionality or make your own new one, since this is VERY basic and inefficient.
            Like, for real.

            Args:
                unit (unit): The unit that will be moving.
                x (int): The x coordinate of the destination.
                y (int): The y coordinate of the destination.
        """
        # Gets the sun from the list of bodies.
        sun = self.game.bodies[2]

        while unit.moves >= 1:
            if unit.safe(x, y) and unit.energy >= math.ceil((self.distance(unit.x, unit.y, x, y) / self.game.dash_distance) * self.game.dash_cost):
                # Dashes if it is safe to dash to the point and we have enough energy to dash there.
                unit.dash(x, y)

                # Breaks out of the loop since we can't do anything else now.
                break
            else:
                # Otherwise tries moving towards the target.

                # The x and y modifiers for movement.
                x_mod = 0
                y_mod = 0

                if unit.x < x or (y < sun.y and unit.y > sun.y or y > sun.y and unit.y < sun.y) and x > sun.x:
                    # Move to the right if the destination is to the right or on the other side of the sun on the right side.
                    x_mod = 1
                elif unit.x > x or (y < sun.y and unit.y > sun.y or y > sun.y and unit.y < sun.y) and x < sun.x:
                    # Move to the left if the destination is to the left or on the other side of the sun on the left side.
                    x_mod = -1

                if unit.y < y or (x < sun.x and unit.x > sun.x or x > sun.x and unit.x < sun.x) and y > sun.y:
                    # Move down if the destination is down or on the other side of the sun on the lower side.
                    y_mod = 1
                elif unit.y > y or (x < sun.x and unit.x > sun.x or x > sun.x and unit.x < sun.x) and y < sun.y:
                    # Move up if the destination is up or on the other side of the sun on the upper side.
                    y_mod = -1

                if x_mod != 0 and y_mod != 0 and not unit.safe(unit.x + x_mod, unit.y + y_mod):
                    # Special case if we cannot safely move diagonally.
                    if unit.safe(unit.x + x_mod, unit.y):
                        # Only move horizontally if it is safe.
                        y_mod = 0
                    elif unit.safe(unit.x, unit.y + y_mod):
                        # Only move vertically if it is safe.
                        x_mod = 0

                if unit.moves < math.sqrt(2) and x_mod != 0 and y_mod != 0:
                    # Special case if we only have 1 move left and are trying to move 2.
                    if unit.safe(unit.x + x_mod, unit.y):
                        y_mod = 0
                    elif unit.safe(unit.x, unit.y + y_mod):
                        x_mod = 0
                    else:
                        break

                if (x_mod != 0 or y_mod != 0) and (math.sqrt(math.pow(x_mod, 2) + math.pow(y_mod, 2)) >= unit.moves):
                    # Tries to move if either of the modifiers is not zero (we are actually moving somewhere).
                    unit.move(unit.x + x_mod, unit.y + y_mod)
                else:
                    # Breaks otherwise, since something probably went wrong.
                    break
    # <<-- /Creer-Merge: functions -->>
