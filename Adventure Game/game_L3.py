answer = input("Do you like to play? (yes/no) ")

if answer.lower().strip() == 'yes':
    print("Welcome to the world of chaos. You are one of the few survivors in a zombie apocalypse. Your mission is to find a safe haven, but the path is treacherous.")
    
    answer = input("You are at a crossroads. Would you like to take right, left, or go straight? (right/left/straight) ").lower().strip()

    if answer == 'left':
        answer = input("You encounter a group of zombies. Do you want to sneak past them, fight them, or climb a nearby tree? (sneak/fight/climb) ").lower().strip()

        if answer == 'fight':
            print("Brave but foolish. The zombies overwhelm you. You lost ):")

        elif answer == 'sneak':
            print("You successfully sneak past the zombies and find an abandoned house.")
            answer = input("Do you want to search the house for supplies, keep moving, or set a trap for zombies? (search/move/trap) ").lower().strip()

            if answer == 'search':
                print("You find useful supplies and a map. This will help you in your journey. Keep going!")
                answer = input("You hear noises upstairs. Do you investigate, leave the house immediately, or barricade yourself in a room? (investigate/leave/barricade) ").lower().strip()

                if answer == 'investigate':
                    print("You find a survivor who joins your quest. Together, you are stronger. Keep going!")
                    answer = input("You and your new companion reach another crossroads. Do you take the forest path, the river path, or the mountain path? (forest/river/mountain) ").lower().strip()

                    if answer == 'forest':
                        print("The forest is dense and full of dangers. You are ambushed by bandits and lose your supplies. You lost ):")

                    elif answer == 'river':
                        print("You follow the river and find a boat. It’s risky but could be faster. Keep going!")
                        answer = input("Do you take the boat, follow the river on foot, or build a raft? (boat/foot/raft) ").lower().strip()

                        if answer == 'boat':
                            print("The boat capsizes in a storm. You barely make it to shore, losing your supplies. You lost ):")

                        elif answer == 'foot':
                            print("You reach a small town. It looks deserted but you must be cautious. Keep going!")
                            answer = input("Do you search the town for other survivors, find a place to rest, or look for a vehicle? (search/rest/vehicle) ").lower().strip()

                            if answer == 'search':
                                print("You find a group of survivors who welcome you. Together, you make plans to reach the safe haven. Keep going!")
                                answer = input("Do you trust them and follow their plan, suggest your own, or go alone? (trust/suggest/alone) ").lower().strip()

                                if answer == 'trust':
                                    print("They betray you and take your supplies. You lost ):")

                                elif answer == 'suggest':
                                    print("They agree to follow your plan. After a long and dangerous journey, you finally reach the safe haven. Congratulations, you won!")

                                elif answer == 'alone':
                                    print("You face numerous challenges alone and ultimately don't make it. You lost ):")

                            elif answer == 'rest':
                                print("While resting, you are ambushed by zombies. You lost ):")

                            elif answer == 'vehicle':
                                print("The noise of starting the vehicle attracts zombies. You lost ):")

                        elif answer == 'raft':
                            print("The raft is too flimsy and falls apart. You lost ):")

                    elif answer == 'mountain':
                        print("The mountain path is treacherous and you fall to your death. You lost ):")

                elif answer == 'leave':
                    print("You leave the house and continue your journey alone. Without the supplies, your chances are slim. You lost ):")

                elif answer == 'barricade':
                    print("You are safe for now, but trapped. Eventually, you run out of food and water. You lost ):")

            elif answer == 'move':
                print("You miss out on important supplies and a potential ally. Your journey is much harder. You lost ):")

            elif answer == 'trap':
                print("The zombies overpower your trap and find you. You lost ):")

        elif answer == 'climb':
            print("You climb the tree and wait until the zombies leave. You continue your journey but are very tired. Keep going!")
            answer = input("You reach a fork in the path. Do you take the hill path, the cave path, or the river path? (hill/cave/river) ").lower().strip()

            if answer == 'hill':
                print("The hill is steep and you fall. You lost ):")

            elif answer == 'cave':
                print("The cave is dark and full of dangers. You are attacked by wild animals. You lost ):")

            elif answer == 'river':
                print("You follow the river and find a boat. It’s risky but could be faster. Keep going!")
                answer = input("Do you take the boat, follow the river on foot, or build a raft? (boat/foot/raft) ").lower().strip()

                if answer == 'boat':
                    print("The boat capsizes in a storm. You barely make it to shore, losing your supplies. You lost ):")

                elif answer == 'foot':
                    print("You reach a small town. It looks deserted but you must be cautious. Keep going!")
                    answer = input("Do you search the town for other survivors, find a place to rest, or look for a vehicle? (search/rest/vehicle) ").lower().strip()

                    if answer == 'search':
                        print("You find a group of survivors who welcome you. Together, you make plans to reach the safe haven. Keep going!")
                        answer = input("Do you trust them and follow their plan, suggest your own, or go alone? (trust/suggest/alone) ").lower().strip()

                        if answer == 'trust':
                            print("They betray you and take your supplies. You lost ):")

                        elif answer == 'suggest':
                            print("They agree to follow your plan. After a long and dangerous journey, you finally reach the safe haven. Congratulations, you won!")

                        elif answer == 'alone':
                            print("You face numerous challenges alone and ultimately don't make it. You lost ):")

                    elif answer == 'rest':
                        print("While resting, you are ambushed by zombies. You lost ):")

                    elif answer == 'vehicle':
                        print("The noise of starting the vehicle attracts zombies. You lost ):")

                elif answer == 'raft':
                    print("The raft is too flimsy and falls apart. You lost ):")

    elif answer == 'right':
        answer = input("You find a wounded person. Do you help them, ignore them, or take their supplies? (help/ignore/take) ").lower().strip()

        if answer == 'help':
            print("They are grateful and give you useful information about a nearby safe house. Keep going!")
            answer = input("Do you go to the safe house, continue on your planned route, or follow a new path they suggest? (safe house/route/new path) ").lower().strip()

            if answer == 'safe house':
                print("The safe house is a trap set by bandits. You lost ):")

            elif answer == 'route':
                print("You avoid the trap and continue your journey. Keep going!")
                answer = input("You find a car with the keys in it. Do you take the car, continue on foot, or look for another way? (car/foot/another way) ").lower().strip()

                if answer == 'car':
                    print("The car draws too much attention and you are overwhelmed by zombies. You lost ):")

                elif answer == 'foot':
                    print("You stay under the radar and make good progress. Keep going!")
                    answer = input("You meet another survivor who offers to guide you. Do you trust them, go alone, or interrogate them first? (trust/alone/interrogate) ").lower().strip()

                    if answer == 'trust':
                        print("They lead you into a trap. You lost ):")

                    elif answer == 'alone':
                        print("You manage to navigate through the dangers alone and finally reach the safe haven. Congratulations, you won!")

                    elif answer == 'interrogate':
                        print("They turn out to be trustworthy and lead you safely to the haven. Congratulations, you won!")

                elif answer == 'another way':
                    print("You get lost and run out of supplies. You lost ):")

            elif answer == 'new path':
                print("The path leads to a dead end and you are trapped. You lost ):")

        elif answer == 'ignore':
            print("You miss out on crucial information and your journey becomes much harder. You lost ):")

        elif answer == 'take':
            print("You take their supplies but the noise attracts zombies. You lost ):")

    elif answer == 'straight':
        answer = input("You see a group of zombies ahead. Do you sneak past them, fight them, or take a detour? (sneak/fight/detour) ").lower().strip()

        if answer == 'sneak':
            print("You successfully sneak past the zombies but end up in a dangerous area. Keep going!")
            answer = input("You reach an abandoned building. Do you enter it, bypass it, or search around it? (enter/bypass/search) ").lower().strip()

            if answer == 'enter':
                print("The building is a trap set by bandits. You lost ):")

            elif answer == 'bypass':
                print("You safely bypass the building and continue your journey. Keep going!")
                answer = input("You find an old map. Do you follow it, ignore it, or modify your route based on it? (follow/ignore/modify) ").lower().strip()

                if answer == 'follow':
                    print("The map leads you to a dead end. You lost ):")

                elif answer == 'ignore':
                    print("You miss out on helpful information. Your journey becomes much harder. You lost ):")

                elif answer == 'modify':
                    print("Using the map, you find a better route and finally reach the safe haven. Congratulations, you won!")

            elif answer == 'search':
                print("You find useful supplies and continue your journey. Keep going!")
                answer = input("You meet another survivor who seems suspicious. Do you trust them, avoid them, or question them? (trust/avoid/question) ").lower().strip()

                if answer == 'trust':
                    print("They betray you and take your supplies. You lost ):")

                elif answer == 'avoid':
                    print("You avoid potential danger and continue your journey alone. You finally reach the safe haven. Congratulations, you won!")

                elif answer == 'question':
                    print("They reveal useful information and you join forces to reach the safe haven. Congratulations, you won!")

        elif answer == 'fight':
            print("Brave but foolish. The zombies overwhelm you. You lost ):")

        elif answer == 'detour':
            print("The detour is long and you run out of supplies. You lost ):")

    else:
        print("Invalid choice, you lost!")

else:
    print("That's too bad")
