# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status, location_cows, season, slurry_tank, grass_status):
    take_cows = True if (time_of_day == 'night' and location_cows == 'pasture') or (location_cows == 'pasture' and weather == 'rainy') else False
    milk_cows = True if cow_milking_status == True and location_cows =='cowshed' else False
    slurry_action = True if slurry_tank == True and location_cows == 'cowshed' and weather != ('sunny' or 'windy') else False
    grass_action = True if grass_status == True and season == 'spring' and weather == 'sunny' and location_cows != 'pasture' else False
    if take_cows == True:
        action = 'take cows to cowshed'
        return action
    elif milk_cows == True:
        action = 'milk cows'
        return action
    elif slurry_action == True:
        action = 'fertilize pasture'
        return action
    elif grass_action == True:
        action = 'mow grass'
        return action
    elif location_cows != 'cowshed':
        action1 = '\nmilk cows' if cow_milking_status == True else ''
        action2 = '\nfertilize pasture' if (slurry_tank == True and weather != ('sunny' or 'windy')) == True else ''
        action3 = '\nmow grass' if grass_status == True and season == 'spring' and weather == 'sunny' else ''
        action = str('take cows to cowshed'+action1+action2+action3+'\ntake cows back to pasture')
        return action
    else:
        action = 'wait'
        return action
    
#    return action5

test = farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
print(test)