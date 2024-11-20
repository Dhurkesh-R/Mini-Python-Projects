answer = input("Do you like to play? (yes/no) ")

if answer.lower().strip() == 'yes':
    print("Welcome to the world of chaos. You are one of the few survivors in a zombie apocalypse. Your mission is to find a safe haven, but the path is treacherous.")
    
    answer = input("You are at a crossroads. Would you like to take right or left? (right/left) ").lower().strip()

    if answer == 'left':
        answer = input("You encounter a group of zombies. Do you want to sneak past them or fight them? (sneak/fight) ").lower().strip()

        if answer == 'fight':
            print("Brave but foolish. The zombies overwhelm you. You lost ):")

        elif answer == 'sneak':
            print("You successfully sneak past the zombies and find an abandoned house.")
            answer = input("Do you want to search the house for supplies or keep moving? (search/move) ").lower().strip()

            if answer == 'search':
                print("You find useful supplies and a map. This will help you in your journey. Keep going!")
                answer = input("You hear noises upstairs. Do you investigate or leave the house immediately? (investigate/leave) ").lower().strip()

                if answer == 'investigate':
                    print("You find a survivor who joins your quest. Together, you are stronger. Keep going!")
                    answer = input("You and your new companion reach another crossroads. Do you take the forest path or the river path? (forest/river) ").lower().strip()

                    if answer == 'forest':
                        print("The forest is dense and full of dangers. You are ambushed by bandits and lose your supplies. You lost ):")

                    elif answer == 'river':
                        print("You follow the river and find a boat. It’s risky but could be faster. Keep going!")
                        answer = input("Do you take the boat or follow the river on foot? (boat/foot) ").lower().strip()

                        if answer == 'boat':
                            print("The boat capsizes in a storm. You barely make it to shore, losing your supplies. You lost ):")

                        elif answer == 'foot':
                            print("You reach a small town. It looks deserted but you must be cautious. Keep going!")
                            answer = input("Do you search the town for other survivors or find a place to rest? (search/rest) ").lower().strip()

                            if answer == 'search':
                                print("You find a group of survivors who welcome you. Together, you make plans to reach the safe haven. Keep going!")
                                answer = input("Do you trust them and follow their plan or suggest your own? (trust/suggest) ").lower().strip()

                                if answer == 'trust':
                                    print("They betray you and take your supplies. You lost ):")

                                elif answer == 'suggest':
                                    print("They agree to follow your plan. After a long and dangerous journey, you finally reach the safe haven. Congratulations, you won!")

                            elif answer == 'rest':
                                print("While resting, you are ambushed by zombies. You lost ):")

                elif answer == 'leave':
                    print("You leave the house and continue your journey alone. Without the supplies, your chances are slim. You lost ):")

            elif answer == 'move':
                print("You miss out on important supplies and a potential ally. Your journey is much harder. You lost ):")

    elif answer == 'right':
        answer = input("You find a wounded person. Do you help them or ignore them? (help/ignore) ").lower().strip()

        if answer == 'help':
            print("They are grateful and give you useful information about a nearby safe house. Keep going!")
            answer = input("Do you go to the safe house or continue on your planned route? (safe house/route) ").lower().strip()

            if answer == 'safe house':
                print("The safe house is a trap set by bandits. You lost ):")

            elif answer == 'route':
                print("You avoid the trap and continue your journey. Keep going!")
                answer = input("You find a car with the keys in it. Do you take the car or continue on foot? (car/foot) ").lower().strip()

                if answer == 'car':
                    print("The car draws too much attention and you are overwhelmed by zombies. You lost ):")

                elif answer == 'foot':
                    print("You stay under the radar and make good progress. Keep going!")
                    answer = input("You meet another survivor who offers to guide you. Do you trust them or go alone? (trust/alone) ").lower().strip()

                    if answer == 'trust':
                        print("They lead you into a trap. You lost ):")

                    elif answer == 'alone':
                        print("You manage to navigate through the dangers alone and finally reach the safe haven. Congratulations, you won!")

        elif answer == 'ignore':
            print("You miss out on crucial information and your journey becomes much harder. You lost ):")

    else:
        print("Invalid choice, you lost!")

else:
    print("That's too bad")
