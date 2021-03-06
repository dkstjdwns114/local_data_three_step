from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']


def data():
    # 19λλ close λΆλ₯
    animal_close_19 = theoremLocalDataClose19['animal']
    culture_close_19 = theoremLocalDataClose19['culture']
    environment_close_19 = theoremLocalDataClose19['environment']
    food_close_19 = theoremLocalDataClose19['food']
    health_close_19 = theoremLocalDataClose19['health']
    life_close_19 = theoremLocalDataClose19['life']
    other_close_19 = theoremLocalDataClose19['other']

    animal_animal_close_19_cnt = 0
    animal_animal_husbandry_close_19_cnt = 0
    for store in animal_close_19.find({}):
        if store['open_service_id'][0:5] == "02_03":
            animal_animal_close_19_cnt += 1
            print(animal_animal_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "02_04":
            animal_animal_husbandry_close_19_cnt += 1
            print(animal_animal_husbandry_close_19_cnt, store)

    culture_game_close_19_cnt = 0
    culture_show_close_19_cnt = 0
    culture_tourism_close_19_cnt = 0
    culture_culture_planning_close_19_cnt = 0
    culture_karaoke_close_19_cnt = 0
    culture_video_close_19_cnt = 0
    culture_accommodation_close_19_cnt = 0
    culture_travel_close_19_cnt = 0
    culture_movie_close_19_cnt = 0
    culture_music_close_19_cnt = 0
    for store in culture_close_19.find({}):
        if store['open_service_id'][0:5] == "03_05":
            culture_game_close_19_cnt += 1
            print(culture_game_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_06":
            culture_show_close_19_cnt += 1
            print(culture_show_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_07":
            culture_tourism_close_19_cnt += 1
            print(culture_tourism_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_08":
            culture_culture_planning_close_19_cnt += 1
            print(culture_culture_planning_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_09":
            culture_karaoke_close_19_cnt += 1
            print(culture_karaoke_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_10":
            culture_video_close_19_cnt += 1
            print(culture_video_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_11":
            culture_accommodation_close_19_cnt += 1
            print(culture_accommodation_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_12":
            culture_travel_close_19_cnt += 1
            print(culture_travel_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_13":
            culture_movie_close_19_cnt += 1
            print(culture_movie_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_14":
            culture_music_close_19_cnt += 1
            print(culture_music_close_19_cnt, store)

    environment_wood_close_19_cnt = 0
    environment_energy_close_19_cnt = 0
    environment_groundwater_close_19_cnt = 0
    environment_environment_management_close_19_cnt = 0
    for store in environment_close_19.find({}):
        if store['open_service_id'][0:5] == "09_27":
            environment_wood_close_19_cnt += 1
            print(environment_wood_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_28":
            environment_energy_close_19_cnt += 1
            print(environment_energy_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_29":
            environment_groundwater_close_19_cnt += 1
            print(environment_groundwater_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_30":
            environment_environment_management_close_19_cnt += 1
            print(environment_environment_management_close_19_cnt, store)

    food_school_meals_close_19_cnt = 0
    food_food_close_19_cnt = 0
    food_entertainment_bar_close_19_cnt = 0
    food_restaurant_close_19_cnt = 0
    for store in food_close_19.find({}):
        if store['open_service_id'][0:5] == "07_21":
            food_school_meals_close_19_cnt += 1
            print(food_school_meals_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_22":
            food_food_close_19_cnt += 1
            print(food_food_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_23":
            food_entertainment_bar_close_19_cnt += 1
            print(food_entertainment_bar_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_24":
            food_restaurant_close_19_cnt += 1
            print(food_restaurant_close_19_cnt, store)

    health_healthcare_facility_close_19_cnt = 0
    health_medical_appliances_close_19_cnt = 0
    for store in health_close_19.find({}):
        if store['open_service_id'][0:5] == "01_01":
            health_healthcare_facility_close_19_cnt += 1
            print(health_healthcare_facility_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "01_02":
            health_medical_appliances_close_19_cnt += 1
            print(health_medical_appliances_close_19_cnt, store)

    life_salon_close_19_cnt = 0
    life_laundry_close_19_cnt = 0
    life_distribution_close_19_cnt = 0
    life_physical_education_close_19_cnt = 0
    life_bathhouse_close_19_cnt = 0
    for store in life_close_19.find({}):
        if store['open_service_id'][0:2] == "05":
            life_salon_close_19_cnt += 1
            print(life_salon_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "06_20":
            life_laundry_close_19_cnt += 1
            print(life_laundry_close_19_cnt, store)
        elif store['open_service_id'][0:2] == "08":
            life_distribution_close_19_cnt += 1
            print(life_distribution_close_19_cnt, store)
        elif store['open_service_id'][0:2] == "10":
            life_physical_education_close_19_cnt += 1
            print(life_physical_education_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_44":
            life_bathhouse_close_19_cnt += 1
            print(life_bathhouse_close_19_cnt, store)

    other_media_close_19_cnt = 0
    other_cigarette_close_19_cnt = 0
    other_logistics_close_19_cnt = 0
    other_civil_defense_close_19_cnt = 0
    other_funeral_close_19_cnt = 0
    other_elevator_close_19_cnt = 0
    other_educational_institutions_close_19_cnt = 0
    other_office_support_close_19_cnt = 0
    for store in other_close_19.find({}):
        if store['open_service_id'][0:2] == "04":
            other_media_close_19_cnt += 1
            print(other_media_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_43":
            other_cigarette_close_19_cnt += 1
            print(other_cigarette_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_45":
            other_logistics_close_19_cnt += 1
            print(other_logistics_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_46":
            other_civil_defense_close_19_cnt += 1
            print(other_civil_defense_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_47":
            other_funeral_close_19_cnt += 1
            print(other_funeral_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_48":
            other_elevator_close_19_cnt += 1
            print(other_elevator_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_49":
            other_educational_institutions_close_19_cnt += 1
            print(other_educational_institutions_close_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_50":
            other_office_support_close_19_cnt += 1
            print(other_office_support_close_19_cnt, store)

    # 19λλ open λΆλ₯
    animal_open_19 = theoremLocalDataOpen19['animal']
    culture_open_19 = theoremLocalDataOpen19['culture']
    environment_open_19 = theoremLocalDataOpen19['environment']
    food_open_19 = theoremLocalDataOpen19['food']
    health_open_19 = theoremLocalDataOpen19['health']
    life_open_19 = theoremLocalDataOpen19['life']
    other_open_19 = theoremLocalDataOpen19['other']

    animal_animal_open_19_cnt = 0
    animal_animal_husbandry_open_19_cnt = 0
    for store in animal_open_19.find({}):
        if store['open_service_id'][0:5] == "02_03":
            animal_animal_open_19_cnt += 1
            print(animal_animal_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "02_04":
            animal_animal_husbandry_open_19_cnt += 1
            print(animal_animal_husbandry_open_19_cnt, store)

    culture_game_open_19_cnt = 0
    culture_show_open_19_cnt = 0
    culture_tourism_open_19_cnt = 0
    culture_culture_planning_open_19_cnt = 0
    culture_karaoke_open_19_cnt = 0
    culture_video_open_19_cnt = 0
    culture_accommodation_open_19_cnt = 0
    culture_travel_open_19_cnt = 0
    culture_movie_open_19_cnt = 0
    culture_music_open_19_cnt = 0
    for store in culture_open_19.find({}):
        if store['open_service_id'][0:5] == "03_05":
            culture_game_open_19_cnt += 1
            print(culture_game_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_06":
            culture_show_open_19_cnt += 1
            print(culture_show_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_07":
            culture_tourism_open_19_cnt += 1
            print(culture_tourism_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_08":
            culture_culture_planning_open_19_cnt += 1
            print(culture_culture_planning_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_09":
            culture_karaoke_open_19_cnt += 1
            print(culture_karaoke_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_10":
            culture_video_open_19_cnt += 1
            print(culture_video_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_11":
            culture_accommodation_open_19_cnt += 1
            print(culture_accommodation_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_12":
            culture_travel_open_19_cnt += 1
            print(culture_travel_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_13":
            culture_movie_open_19_cnt += 1
            print(culture_movie_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "03_14":
            culture_music_open_19_cnt += 1
            print(culture_music_open_19_cnt, store)

    environment_wood_open_19_cnt = 0
    environment_energy_open_19_cnt = 0
    environment_groundwater_open_19_cnt = 0
    environment_environment_management_open_19_cnt = 0
    for store in environment_open_19.find({}):
        if store['open_service_id'][0:5] == "09_27":
            environment_wood_open_19_cnt += 1
            print(environment_wood_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_28":
            environment_energy_open_19_cnt += 1
            print(environment_energy_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_29":
            environment_groundwater_open_19_cnt += 1
            print(environment_groundwater_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "09_30":
            environment_environment_management_open_19_cnt += 1
            print(environment_environment_management_open_19_cnt, store)

    food_school_meals_open_19_cnt = 0
    food_food_open_19_cnt = 0
    food_entertainment_bar_open_19_cnt = 0
    food_restaurant_open_19_cnt = 0
    for store in food_open_19.find({}):
        if store['open_service_id'][0:5] == "07_21":
            food_school_meals_open_19_cnt += 1
            print(food_school_meals_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_22":
            food_food_open_19_cnt += 1
            print(food_food_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_23":
            food_entertainment_bar_open_19_cnt += 1
            print(food_entertainment_bar_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "07_24":
            food_restaurant_open_19_cnt += 1
            print(food_restaurant_open_19_cnt, store)

    health_healthcare_facility_open_19_cnt = 0
    health_medical_appliances_open_19_cnt = 0
    for store in health_open_19.find({}):
        if store['open_service_id'][0:5] == "01_01":
            health_healthcare_facility_open_19_cnt += 1
            print(health_healthcare_facility_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "01_02":
            health_medical_appliances_open_19_cnt += 1
            print(health_medical_appliances_open_19_cnt, store)

    life_salon_open_19_cnt = 0
    life_laundry_open_19_cnt = 0
    life_distribution_open_19_cnt = 0
    life_physical_education_open_19_cnt = 0
    life_bathhouse_open_19_cnt = 0
    for store in life_open_19.find({}):
        if store['open_service_id'][0:2] == "05":
            life_salon_open_19_cnt += 1
            print(life_salon_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "06_20":
            life_laundry_open_19_cnt += 1
            print(life_laundry_open_19_cnt, store)
        elif store['open_service_id'][0:2] == "08":
            life_distribution_open_19_cnt += 1
            print(life_distribution_open_19_cnt, store)
        elif store['open_service_id'][0:2] == "10":
            life_physical_education_open_19_cnt += 1
            print(life_physical_education_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_44":
            life_bathhouse_open_19_cnt += 1
            print(life_bathhouse_open_19_cnt, store)

    other_media_open_19_cnt = 0
    other_cigarette_open_19_cnt = 0
    other_logistics_open_19_cnt = 0
    other_civil_defense_open_19_cnt = 0
    other_funeral_open_19_cnt = 0
    other_elevator_open_19_cnt = 0
    other_educational_institutions_open_19_cnt = 0
    other_office_support_open_19_cnt = 0
    for store in other_open_19.find({}):
        if store['open_service_id'][0:2] == "04":
            other_media_open_19_cnt += 1
            print(other_media_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_43":
            other_cigarette_open_19_cnt += 1
            print(other_cigarette_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_45":
            other_logistics_open_19_cnt += 1
            print(other_logistics_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_46":
            other_civil_defense_open_19_cnt += 1
            print(other_civil_defense_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_47":
            other_funeral_open_19_cnt += 1
            print(other_funeral_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_48":
            other_elevator_open_19_cnt += 1
            print(other_elevator_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_49":
            other_educational_institutions_open_19_cnt += 1
            print(other_educational_institutions_open_19_cnt, store)
        elif store['open_service_id'][0:5] == "11_50":
            other_office_support_open_19_cnt += 1
            print(other_office_support_open_19_cnt, store)

    # 20λλ close λΆλ₯
    animal_close_20 = theoremLocalDataClose20['animal']
    culture_close_20 = theoremLocalDataClose20['culture']
    environment_close_20 = theoremLocalDataClose20['environment']
    food_close_20 = theoremLocalDataClose20['food']
    health_close_20 = theoremLocalDataClose20['health']
    life_close_20 = theoremLocalDataClose20['life']
    other_close_20 = theoremLocalDataClose20['other']

    animal_animal_close_20_cnt = 0
    animal_animal_husbandry_close_20_cnt = 0
    for store in animal_close_20.find({}):
        if store['open_service_id'][0:5] == "02_03":
            animal_animal_close_20_cnt += 1
            print(animal_animal_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "02_04":
            animal_animal_husbandry_close_20_cnt += 1
            print(animal_animal_husbandry_close_20_cnt, store)

    culture_game_close_20_cnt = 0
    culture_show_close_20_cnt = 0
    culture_tourism_close_20_cnt = 0
    culture_culture_planning_close_20_cnt = 0
    culture_karaoke_close_20_cnt = 0
    culture_video_close_20_cnt = 0
    culture_accommodation_close_20_cnt = 0
    culture_travel_close_20_cnt = 0
    culture_movie_close_20_cnt = 0
    culture_music_close_20_cnt = 0
    for store in culture_close_20.find({}):
        if store['open_service_id'][0:5] == "03_05":
            culture_game_close_20_cnt += 1
            print(culture_game_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_06":
            culture_show_close_20_cnt += 1
            print(culture_show_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_07":
            culture_tourism_close_20_cnt += 1
            print(culture_tourism_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_08":
            culture_culture_planning_close_20_cnt += 1
            print(culture_culture_planning_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_09":
            culture_karaoke_close_20_cnt += 1
            print(culture_karaoke_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_10":
            culture_video_close_20_cnt += 1
            print(culture_video_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_11":
            culture_accommodation_close_20_cnt += 1
            print(culture_accommodation_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_12":
            culture_travel_close_20_cnt += 1
            print(culture_travel_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_13":
            culture_movie_close_20_cnt += 1
            print(culture_movie_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_14":
            culture_music_close_20_cnt += 1
            print(culture_music_close_20_cnt, store)

    environment_wood_close_20_cnt = 0
    environment_energy_close_20_cnt = 0
    environment_groundwater_close_20_cnt = 0
    environment_environment_management_close_20_cnt = 0
    for store in environment_close_20.find({}):
        if store['open_service_id'][0:5] == "09_27":
            environment_wood_close_20_cnt += 1
            print(environment_wood_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_28":
            environment_energy_close_20_cnt += 1
            print(environment_energy_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_29":
            environment_groundwater_close_20_cnt += 1
            print(environment_groundwater_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_30":
            environment_environment_management_close_20_cnt += 1
            print(environment_environment_management_close_20_cnt, store)

    food_school_meals_close_20_cnt = 0
    food_food_close_20_cnt = 0
    food_entertainment_bar_close_20_cnt = 0
    food_restaurant_close_20_cnt = 0
    for store in food_close_20.find({}):
        if store['open_service_id'][0:5] == "07_21":
            food_school_meals_close_20_cnt += 1
            print(food_school_meals_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_22":
            food_food_close_20_cnt += 1
            print(food_food_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_23":
            food_entertainment_bar_close_20_cnt += 1
            print(food_entertainment_bar_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_24":
            food_restaurant_close_20_cnt += 1
            print(food_restaurant_close_20_cnt, store)

    health_healthcare_facility_close_20_cnt = 0
    health_medical_appliances_close_20_cnt = 0
    for store in health_close_20.find({}):
        if store['open_service_id'][0:5] == "01_01":
            health_healthcare_facility_close_20_cnt += 1
            print(health_healthcare_facility_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "01_02":
            health_medical_appliances_close_20_cnt += 1
            print(health_medical_appliances_close_20_cnt, store)

    life_salon_close_20_cnt = 0
    life_laundry_close_20_cnt = 0
    life_distribution_close_20_cnt = 0
    life_physical_education_close_20_cnt = 0
    life_bathhouse_close_20_cnt = 0
    for store in life_close_20.find({}):
        if store['open_service_id'][0:2] == "05":
            life_salon_close_20_cnt += 1
            print(life_salon_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "06_20":
            life_laundry_close_20_cnt += 1
            print(life_laundry_close_20_cnt, store)
        elif store['open_service_id'][0:2] == "08":
            life_distribution_close_20_cnt += 1
            print(life_distribution_close_20_cnt, store)
        elif store['open_service_id'][0:2] == "10":
            life_physical_education_close_20_cnt += 1
            print(life_physical_education_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_44":
            life_bathhouse_close_20_cnt += 1
            print(life_bathhouse_close_20_cnt, store)

    other_media_close_20_cnt = 0
    other_cigarette_close_20_cnt = 0
    other_logistics_close_20_cnt = 0
    other_civil_defense_close_20_cnt = 0
    other_funeral_close_20_cnt = 0
    other_elevator_close_20_cnt = 0
    other_educational_institutions_close_20_cnt = 0
    other_office_support_close_20_cnt = 0
    for store in other_close_20.find({}):
        if store['open_service_id'][0:2] == "04":
            other_media_close_20_cnt += 1
            print(other_media_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_43":
            other_cigarette_close_20_cnt += 1
            print(other_cigarette_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_45":
            other_logistics_close_20_cnt += 1
            print(other_logistics_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_46":
            other_civil_defense_close_20_cnt += 1
            print(other_civil_defense_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_47":
            other_funeral_close_20_cnt += 1
            print(other_funeral_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_48":
            other_elevator_close_20_cnt += 1
            print(other_elevator_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_49":
            other_educational_institutions_close_20_cnt += 1
            print(other_educational_institutions_close_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_50":
            other_office_support_close_20_cnt += 1
            print(other_office_support_close_20_cnt, store)

    # 20λλ open λΆλ₯
    animal_open_20 = theoremLocalDataOpen20['animal']
    culture_open_20 = theoremLocalDataOpen20['culture']
    environment_open_20 = theoremLocalDataOpen20['environment']
    food_open_20 = theoremLocalDataOpen20['food']
    health_open_20 = theoremLocalDataOpen20['health']
    life_open_20 = theoremLocalDataOpen20['life']
    other_open_20 = theoremLocalDataOpen20['other']

    animal_animal_open_20_cnt = 0
    animal_animal_husbandry_open_20_cnt = 0
    for store in animal_open_20.find({}):
        if store['open_service_id'][0:5] == "02_03":
            animal_animal_open_20_cnt += 1
            print(animal_animal_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "02_04":
            animal_animal_husbandry_open_20_cnt += 1
            print(animal_animal_husbandry_open_20_cnt, store)

    culture_game_open_20_cnt = 0
    culture_show_open_20_cnt = 0
    culture_tourism_open_20_cnt = 0
    culture_culture_planning_open_20_cnt = 0
    culture_karaoke_open_20_cnt = 0
    culture_video_open_20_cnt = 0
    culture_accommodation_open_20_cnt = 0
    culture_travel_open_20_cnt = 0
    culture_movie_open_20_cnt = 0
    culture_music_open_20_cnt = 0
    for store in culture_open_20.find({}):
        if store['open_service_id'][0:5] == "03_05":
            culture_game_open_20_cnt += 1
            print(culture_game_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_06":
            culture_show_open_20_cnt += 1
            print(culture_show_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_07":
            culture_tourism_open_20_cnt += 1
            print(culture_tourism_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_08":
            culture_culture_planning_open_20_cnt += 1
            print(culture_culture_planning_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_09":
            culture_karaoke_open_20_cnt += 1
            print(culture_karaoke_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_10":
            culture_video_open_20_cnt += 1
            print(culture_video_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_11":
            culture_accommodation_open_20_cnt += 1
            print(culture_accommodation_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_12":
            culture_travel_open_20_cnt += 1
            print(culture_travel_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_13":
            culture_movie_open_20_cnt += 1
            print(culture_movie_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "03_14":
            culture_music_open_20_cnt += 1
            print(culture_music_open_20_cnt, store)

    environment_wood_open_20_cnt = 0
    environment_energy_open_20_cnt = 0
    environment_groundwater_open_20_cnt = 0
    environment_environment_management_open_20_cnt = 0
    for store in environment_open_20.find({}):
        if store['open_service_id'][0:5] == "09_27":
            environment_wood_open_20_cnt += 1
            print(environment_wood_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_28":
            environment_energy_open_20_cnt += 1
            print(environment_energy_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_29":
            environment_groundwater_open_20_cnt += 1
            print(environment_groundwater_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "09_30":
            environment_environment_management_open_20_cnt += 1
            print(environment_environment_management_open_20_cnt, store)

    food_school_meals_open_20_cnt = 0
    food_food_open_20_cnt = 0
    food_entertainment_bar_open_20_cnt = 0
    food_restaurant_open_20_cnt = 0
    for store in food_open_20.find({}):
        if store['open_service_id'][0:5] == "07_21":
            food_school_meals_open_20_cnt += 1
            print(food_school_meals_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_22":
            food_food_open_20_cnt += 1
            print(food_food_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_23":
            food_entertainment_bar_open_20_cnt += 1
            print(food_entertainment_bar_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "07_24":
            food_restaurant_open_20_cnt += 1
            print(food_restaurant_open_20_cnt, store)

    health_healthcare_facility_open_20_cnt = 0
    health_medical_appliances_open_20_cnt = 0
    for store in health_open_20.find({}):
        if store['open_service_id'][0:5] == "01_01":
            health_healthcare_facility_open_20_cnt += 1
            print(health_healthcare_facility_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "01_02":
            health_medical_appliances_open_20_cnt += 1
            print(health_medical_appliances_open_20_cnt, store)

    life_salon_open_20_cnt = 0
    life_laundry_open_20_cnt = 0
    life_distribution_open_20_cnt = 0
    life_physical_education_open_20_cnt = 0
    life_bathhouse_open_20_cnt = 0
    for store in life_open_20.find({}):
        if store['open_service_id'][0:2] == "05":
            life_salon_open_20_cnt += 1
            print(life_salon_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "06_20":
            life_laundry_open_20_cnt += 1
            print(life_laundry_open_20_cnt, store)
        elif store['open_service_id'][0:2] == "08":
            life_distribution_open_20_cnt += 1
            print(life_distribution_open_20_cnt, store)
        elif store['open_service_id'][0:2] == "10":
            life_physical_education_open_20_cnt += 1
            print(life_physical_education_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_44":
            life_bathhouse_open_20_cnt += 1
            print(life_bathhouse_open_20_cnt, store)

    other_media_open_20_cnt = 0
    other_cigarette_open_20_cnt = 0
    other_logistics_open_20_cnt = 0
    other_civil_defense_open_20_cnt = 0
    other_funeral_open_20_cnt = 0
    other_elevator_open_20_cnt = 0
    other_educational_institutions_open_20_cnt = 0
    other_office_support_open_20_cnt = 0
    for store in other_open_20.find({}):
        if store['open_service_id'][0:2] == "04":
            other_media_open_20_cnt += 1
            print(other_media_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_43":
            other_cigarette_open_20_cnt += 1
            print(other_cigarette_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_45":
            other_logistics_open_20_cnt += 1
            print(other_logistics_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_46":
            other_civil_defense_open_20_cnt += 1
            print(other_civil_defense_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_47":
            other_funeral_open_20_cnt += 1
            print(other_funeral_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_48":
            other_elevator_open_20_cnt += 1
            print(other_elevator_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_49":
            other_educational_institutions_open_20_cnt += 1
            print(other_educational_institutions_open_20_cnt, store)
        elif store['open_service_id'][0:5] == "11_50":
            other_office_support_open_20_cnt += 1
            print(other_office_support_open_20_cnt, store)

    info = {
        "title": "Type Detail",
        "type_detail_close_19": [
            {
                "category": "animal",
                "kor_type": "λλ¬Ό",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "μ μλλ¬Ό",
                        "count": animal_animal_close_19_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "μΆμ°",
                        "count": animal_animal_husbandry_close_19_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "λ¬Έν",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "κ²μ",
                        "count": culture_game_close_19_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "κ³΅μ°",
                        "count": culture_show_close_19_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "κ΄κ΄",
                        "count": culture_tourism_close_19_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "λ¬ΈνκΈ°ν",
                        "count": culture_culture_planning_close_19_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "λΈλλ°©",
                        "count": culture_karaoke_close_19_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "λΉλμ€",
                        "count": culture_video_close_19_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "μλ°",
                        "count": culture_accommodation_close_19_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "μ¬ν",
                        "count": culture_travel_close_19_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "μν",
                        "count": culture_movie_close_19_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "μμ",
                        "count": culture_music_close_19_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "μμ°νκ²½",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "λͺ©μ¬",
                        "count": environment_wood_close_19_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "μλμ§",
                        "count": environment_energy_close_19_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "μ§νμ",
                        "count": environment_groundwater_close_19_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "νκ²½κ΄λ¦¬",
                        "count": environment_environment_management_close_19_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "κΈμ",
                        "count": food_school_meals_close_19_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "μν μ μ‘°/κ°κ³΅/νλ§€",
                        "count": food_food_close_19_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "μ ν₯μ£Όμ /λ¨λμ£Όμ ",
                        "count": food_entertainment_bar_close_19_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "μμμ ",
                        "count": food_restaurant_close_19_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "κ±΄κ°",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "μλ£κΈ°κ΄",
                        "count": health_healthcare_facility_close_19_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "μλ£κΈ°κΈ°",
                        "count": health_medical_appliances_close_19_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "λ―Έμ©/μ΄μ©",
                        "count": life_salon_close_19_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "μΈνμ/λΉ¨λλ°©",
                        "count": life_laundry_close_19_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "μ ν΅",
                        "count": life_distribution_close_19_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "μ²΄μ‘",
                        "count": life_physical_education_close_19_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "λͺ©μν/μ°μ§λ°©/μ¬μ°λ",
                        "count": life_bathhouse_close_19_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "κΈ°ν",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "λ―Έλμ΄",
                        "count": other_media_close_19_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "λ΄λ°°",
                        "count": other_cigarette_close_19_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "λ¬Όλ₯",
                        "count": other_logistics_close_19_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "λ―Όλ°©μ",
                        "count": other_civil_defense_close_19_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "μμ‘°",
                        "count": other_funeral_close_19_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "μλ¦¬λ² μ΄ν°",
                        "count": other_elevator_close_19_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "μ λ¬Έκ΅μ‘κΈ°κ΄",
                        "count": other_educational_institutions_close_19_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "μ¬λ¬΄μ§μ",
                        "count": other_office_support_close_19_cnt
                    }
                ]
            }
        ],
        "type_detail_open_19": [
            {
                "category": "animal",
                "kor_type": "λλ¬Ό",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "μ μλλ¬Ό",
                        "count": animal_animal_open_19_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "μΆμ°",
                        "count": animal_animal_husbandry_open_19_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "λ¬Έν",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "κ²μ",
                        "count": culture_game_open_19_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "κ³΅μ°",
                        "count": culture_show_open_19_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "κ΄κ΄",
                        "count": culture_tourism_open_19_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "λ¬ΈνκΈ°ν",
                        "count": culture_culture_planning_open_19_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "λΈλλ°©",
                        "count": culture_karaoke_open_19_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "λΉλμ€",
                        "count": culture_video_open_19_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "μλ°",
                        "count": culture_accommodation_open_19_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "μ¬ν",
                        "count": culture_travel_open_19_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "μν",
                        "count": culture_movie_open_19_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "μμ",
                        "count": culture_music_open_19_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "μμ°νκ²½",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "λͺ©μ¬",
                        "count": environment_wood_open_19_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "μλμ§",
                        "count": environment_energy_open_19_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "μ§νμ",
                        "count": environment_groundwater_open_19_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "νκ²½κ΄λ¦¬",
                        "count": environment_environment_management_open_19_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "κΈμ",
                        "count": food_school_meals_open_19_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "μν μ μ‘°/κ°κ³΅/νλ§€",
                        "count": food_food_open_19_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "μ ν₯μ£Όμ /λ¨λμ£Όμ ",
                        "count": food_entertainment_bar_open_19_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "μμμ ",
                        "count": food_restaurant_open_19_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "κ±΄κ°",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "μλ£κΈ°κ΄",
                        "count": health_healthcare_facility_open_19_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "μλ£κΈ°κΈ°",
                        "count": health_medical_appliances_open_19_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "λ―Έμ©/μ΄μ©",
                        "count": life_salon_open_19_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "μΈνμ/λΉ¨λλ°©",
                        "count": life_laundry_open_19_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "μ ν΅",
                        "count": life_distribution_open_19_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "μ²΄μ‘",
                        "count": life_physical_education_open_19_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "λͺ©μν/μ°μ§λ°©/μ¬μ°λ",
                        "count": life_bathhouse_open_19_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "κΈ°ν",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "λ―Έλμ΄",
                        "count": other_media_open_19_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "λ΄λ°°",
                        "count": other_cigarette_open_19_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "λ¬Όλ₯",
                        "count": other_logistics_open_19_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "λ―Όλ°©μ",
                        "count": other_civil_defense_open_19_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "μμ‘°",
                        "count": other_funeral_open_19_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "μλ¦¬λ² μ΄ν°",
                        "count": other_elevator_open_19_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "μ λ¬Έκ΅μ‘κΈ°κ΄",
                        "count": other_educational_institutions_open_19_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "μ¬λ¬΄μ§μ",
                        "count": other_office_support_open_19_cnt
                    }
                ]
            }
        ],
        "type_detail_close_20": [
            {
                "category": "animal",
                "kor_type": "λλ¬Ό",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "μ μλλ¬Ό",
                        "count": animal_animal_close_20_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "μΆμ°",
                        "count": animal_animal_husbandry_close_20_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "λ¬Έν",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "κ²μ",
                        "count": culture_game_close_20_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "κ³΅μ°",
                        "count": culture_show_close_20_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "κ΄κ΄",
                        "count": culture_tourism_close_20_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "λ¬ΈνκΈ°ν",
                        "count": culture_culture_planning_close_20_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "λΈλλ°©",
                        "count": culture_karaoke_close_20_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "λΉλμ€",
                        "count": culture_video_close_20_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "μλ°",
                        "count": culture_accommodation_close_20_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "μ¬ν",
                        "count": culture_travel_close_20_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "μν",
                        "count": culture_movie_close_20_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "μμ",
                        "count": culture_music_close_20_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "μμ°νκ²½",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "λͺ©μ¬",
                        "count": environment_wood_close_20_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "μλμ§",
                        "count": environment_energy_close_20_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "μ§νμ",
                        "count": environment_groundwater_close_20_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "νκ²½κ΄λ¦¬",
                        "count": environment_environment_management_close_20_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "κΈμ",
                        "count": food_school_meals_close_20_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "μν μ μ‘°/κ°κ³΅/νλ§€",
                        "count": food_food_close_20_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "μ ν₯μ£Όμ /λ¨λμ£Όμ ",
                        "count": food_entertainment_bar_close_20_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "μμμ ",
                        "count": food_restaurant_close_20_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "κ±΄κ°",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "μλ£κΈ°κ΄",
                        "count": health_healthcare_facility_close_20_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "μλ£κΈ°κΈ°",
                        "count": health_medical_appliances_close_20_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "λ―Έμ©/μ΄μ©",
                        "count": life_salon_close_20_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "μΈνμ/λΉ¨λλ°©",
                        "count": life_laundry_close_20_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "μ ν΅",
                        "count": life_distribution_close_20_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "μ²΄μ‘",
                        "count": life_physical_education_close_20_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "λͺ©μν/μ°μ§λ°©/μ¬μ°λ",
                        "count": life_bathhouse_close_20_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "κΈ°ν",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "λ―Έλμ΄",
                        "count": other_media_close_20_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "λ΄λ°°",
                        "count": other_cigarette_close_20_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "λ¬Όλ₯",
                        "count": other_logistics_close_20_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "λ―Όλ°©μ",
                        "count": other_civil_defense_close_20_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "μμ‘°",
                        "count": other_funeral_close_20_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "μλ¦¬λ² μ΄ν°",
                        "count": other_elevator_close_20_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "μ λ¬Έκ΅μ‘κΈ°κ΄",
                        "count": other_educational_institutions_close_20_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "μ¬λ¬΄μ§μ",
                        "count": other_office_support_close_20_cnt
                    }
                ]
            }
        ],
        "type_detail_open_20": [
            {
                "category": "animal",
                "kor_type": "λλ¬Ό",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "μ μλλ¬Ό",
                        "count": animal_animal_open_20_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "μΆμ°",
                        "count": animal_animal_husbandry_open_20_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "λ¬Έν",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "κ²μ",
                        "count": culture_game_open_20_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "κ³΅μ°",
                        "count": culture_show_open_20_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "κ΄κ΄",
                        "count": culture_tourism_open_20_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "λ¬ΈνκΈ°ν",
                        "count": culture_culture_planning_open_20_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "λΈλλ°©",
                        "count": culture_karaoke_open_20_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "λΉλμ€",
                        "count": culture_video_open_20_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "μλ°",
                        "count": culture_accommodation_open_20_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "μ¬ν",
                        "count": culture_travel_open_20_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "μν",
                        "count": culture_movie_open_20_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "μμ",
                        "count": culture_music_open_20_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "μμ°νκ²½",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "λͺ©μ¬",
                        "count": environment_wood_open_20_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "μλμ§",
                        "count": environment_energy_open_20_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "μ§νμ",
                        "count": environment_groundwater_open_20_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "νκ²½κ΄λ¦¬",
                        "count": environment_environment_management_open_20_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "κΈμ",
                        "count": food_school_meals_open_20_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "μν μ μ‘°/κ°κ³΅/νλ§€",
                        "count": food_food_open_20_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "μ ν₯μ£Όμ /λ¨λμ£Όμ ",
                        "count": food_entertainment_bar_open_20_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "μμμ ",
                        "count": food_restaurant_open_20_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "κ±΄κ°",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "μλ£κΈ°κ΄",
                        "count": health_healthcare_facility_open_20_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "μλ£κΈ°κΈ°",
                        "count": health_medical_appliances_open_20_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "μν",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "λ―Έμ©/μ΄μ©",
                        "count": life_salon_open_20_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "μΈνμ/λΉ¨λλ°©",
                        "count": life_laundry_open_20_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "μ ν΅",
                        "count": life_distribution_open_20_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "μ²΄μ‘",
                        "count": life_physical_education_open_20_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "λͺ©μν/μ°μ§λ°©/μ¬μ°λ",
                        "count": life_bathhouse_open_20_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "κΈ°ν",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "λ―Έλμ΄",
                        "count": other_media_open_20_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "λ΄λ°°",
                        "count": other_cigarette_open_20_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "λ¬Όλ₯",
                        "count": other_logistics_open_20_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "λ―Όλ°©μ",
                        "count": other_civil_defense_open_20_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "μμ‘°",
                        "count": other_funeral_open_20_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "μλ¦¬λ² μ΄ν°",
                        "count": other_elevator_open_20_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "μ λ¬Έκ΅μ‘κΈ°κ΄",
                        "count": other_educational_institutions_open_20_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "μ¬λ¬΄μ§μ",
                        "count": other_office_support_open_20_cnt
                    }
                ]
            }
        ]
    }
    local_main_api = db['local_data_api']
    print("info", info)

    my_api_id = local_main_api.insert_one(info).inserted_id
    print(my_api_id)


data()
