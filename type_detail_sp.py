from pymongo import MongoClient

cluster = MongoClient("mongodb://test1:KQ2DmS5BaPpKIBxL@cluster0-shard-00-00.6v20o.mongodb.net:27017,cluster0-shard-00-01.6v20o.mongodb.net:27017,cluster0-shard-00-02.6v20o.mongodb.net:27017/three-step?ssl=true&replicaSet=atlas-1s13em-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["three-step"]

client = MongoClient("localhost", 27017)

theoremLocalDataClose19 = client['theoremLocalDataClose19']
theoremLocalDataClose20 = client['theoremLocalDataClose20']
theoremLocalDataOpen19 = client['theoremLocalDataOpen19']
theoremLocalDataOpen20 = client['theoremLocalDataOpen20']


def data():
    # 19년도 close 분류
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

    # 19년도 open 분류
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

    # 20년도 close 분류
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

    # 20년도 open 분류
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
                "kor_type": "동물",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "애완동물",
                        "count": animal_animal_close_19_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "축산",
                        "count": animal_animal_husbandry_close_19_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "문화",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "게임",
                        "count": culture_game_close_19_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "공연",
                        "count": culture_show_close_19_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "관광",
                        "count": culture_tourism_close_19_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "문화기획",
                        "count": culture_culture_planning_close_19_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "노래방",
                        "count": culture_karaoke_close_19_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "비디오",
                        "count": culture_video_close_19_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "숙박",
                        "count": culture_accommodation_close_19_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "여행",
                        "count": culture_travel_close_19_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "영화",
                        "count": culture_movie_close_19_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "음악",
                        "count": culture_music_close_19_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "자연환경",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "목재",
                        "count": environment_wood_close_19_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "에너지",
                        "count": environment_energy_close_19_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "지하수",
                        "count": environment_groundwater_close_19_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "환경관리",
                        "count": environment_environment_management_close_19_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "식품",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "급식",
                        "count": food_school_meals_close_19_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "식품 제조/가공/판매",
                        "count": food_food_close_19_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "유흥주점/단란주점",
                        "count": food_entertainment_bar_close_19_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "음식점",
                        "count": food_restaurant_close_19_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "건강",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "의료기관",
                        "count": health_healthcare_facility_close_19_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "의료기기",
                        "count": health_medical_appliances_close_19_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "생활",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "미용/이용",
                        "count": life_salon_close_19_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "세탁소/빨래방",
                        "count": life_laundry_close_19_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "유통",
                        "count": life_distribution_close_19_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "체육",
                        "count": life_physical_education_close_19_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "목욕탕/찜질방/사우나",
                        "count": life_bathhouse_close_19_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "기타",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "미디어",
                        "count": other_media_close_19_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "담배",
                        "count": other_cigarette_close_19_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "물류",
                        "count": other_logistics_close_19_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "민방위",
                        "count": other_civil_defense_close_19_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "상조",
                        "count": other_funeral_close_19_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "엘리베이터",
                        "count": other_elevator_close_19_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "전문교육기관",
                        "count": other_educational_institutions_close_19_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "사무지원",
                        "count": other_office_support_close_19_cnt
                    }
                ]
            }
        ],
        "type_detail_open_19": [
            {
                "category": "animal",
                "kor_type": "동물",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "애완동물",
                        "count": animal_animal_open_19_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "축산",
                        "count": animal_animal_husbandry_open_19_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "문화",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "게임",
                        "count": culture_game_open_19_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "공연",
                        "count": culture_show_open_19_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "관광",
                        "count": culture_tourism_open_19_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "문화기획",
                        "count": culture_culture_planning_open_19_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "노래방",
                        "count": culture_karaoke_open_19_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "비디오",
                        "count": culture_video_open_19_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "숙박",
                        "count": culture_accommodation_open_19_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "여행",
                        "count": culture_travel_open_19_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "영화",
                        "count": culture_movie_open_19_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "음악",
                        "count": culture_music_open_19_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "자연환경",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "목재",
                        "count": environment_wood_open_19_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "에너지",
                        "count": environment_energy_open_19_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "지하수",
                        "count": environment_groundwater_open_19_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "환경관리",
                        "count": environment_environment_management_open_19_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "식품",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "급식",
                        "count": food_school_meals_open_19_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "식품 제조/가공/판매",
                        "count": food_food_open_19_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "유흥주점/단란주점",
                        "count": food_entertainment_bar_open_19_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "음식점",
                        "count": food_restaurant_open_19_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "건강",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "의료기관",
                        "count": health_healthcare_facility_open_19_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "의료기기",
                        "count": health_medical_appliances_open_19_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "생활",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "미용/이용",
                        "count": life_salon_open_19_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "세탁소/빨래방",
                        "count": life_laundry_open_19_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "유통",
                        "count": life_distribution_open_19_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "체육",
                        "count": life_physical_education_open_19_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "목욕탕/찜질방/사우나",
                        "count": life_bathhouse_open_19_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "기타",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "미디어",
                        "count": other_media_open_19_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "담배",
                        "count": other_cigarette_open_19_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "물류",
                        "count": other_logistics_open_19_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "민방위",
                        "count": other_civil_defense_open_19_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "상조",
                        "count": other_funeral_open_19_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "엘리베이터",
                        "count": other_elevator_open_19_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "전문교육기관",
                        "count": other_educational_institutions_open_19_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "사무지원",
                        "count": other_office_support_open_19_cnt
                    }
                ]
            }
        ],
        "type_detail_close_20": [
            {
                "category": "animal",
                "kor_type": "동물",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "애완동물",
                        "count": animal_animal_close_20_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "축산",
                        "count": animal_animal_husbandry_close_20_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "문화",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "게임",
                        "count": culture_game_close_20_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "공연",
                        "count": culture_show_close_20_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "관광",
                        "count": culture_tourism_close_20_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "문화기획",
                        "count": culture_culture_planning_close_20_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "노래방",
                        "count": culture_karaoke_close_20_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "비디오",
                        "count": culture_video_close_20_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "숙박",
                        "count": culture_accommodation_close_20_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "여행",
                        "count": culture_travel_close_20_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "영화",
                        "count": culture_movie_close_20_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "음악",
                        "count": culture_music_close_20_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "자연환경",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "목재",
                        "count": environment_wood_close_20_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "에너지",
                        "count": environment_energy_close_20_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "지하수",
                        "count": environment_groundwater_close_20_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "환경관리",
                        "count": environment_environment_management_close_20_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "식품",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "급식",
                        "count": food_school_meals_close_20_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "식품 제조/가공/판매",
                        "count": food_food_close_20_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "유흥주점/단란주점",
                        "count": food_entertainment_bar_close_20_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "음식점",
                        "count": food_restaurant_close_20_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "건강",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "의료기관",
                        "count": health_healthcare_facility_close_20_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "의료기기",
                        "count": health_medical_appliances_close_20_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "생활",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "미용/이용",
                        "count": life_salon_close_20_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "세탁소/빨래방",
                        "count": life_laundry_close_20_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "유통",
                        "count": life_distribution_close_20_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "체육",
                        "count": life_physical_education_close_20_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "목욕탕/찜질방/사우나",
                        "count": life_bathhouse_close_20_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "기타",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "미디어",
                        "count": other_media_close_20_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "담배",
                        "count": other_cigarette_close_20_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "물류",
                        "count": other_logistics_close_20_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "민방위",
                        "count": other_civil_defense_close_20_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "상조",
                        "count": other_funeral_close_20_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "엘리베이터",
                        "count": other_elevator_close_20_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "전문교육기관",
                        "count": other_educational_institutions_close_20_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "사무지원",
                        "count": other_office_support_close_20_cnt
                    }
                ]
            }
        ],
        "type_detail_open_20": [
            {
                "category": "animal",
                "kor_type": "동물",
                "type_list": [
                    {
                        "type": "animal",
                        "kor_type": "애완동물",
                        "count": animal_animal_open_20_cnt
                    },
                    {
                        "type": "animal_husbandry",
                        "kor_type": "축산",
                        "count": animal_animal_husbandry_open_20_cnt
                    }
                ]
            },
            {
                "category": "culture",
                "kor_type": "문화",
                "type_list": [
                    {
                        "type": "game",
                        "kor_type": "게임",
                        "count": culture_game_open_20_cnt
                    },
                    {
                        "type": "show",
                        "kor_type": "공연",
                        "count": culture_show_open_20_cnt
                    },
                    {
                        "type": "tourism",
                        "kor_type": "관광",
                        "count": culture_tourism_open_20_cnt
                    },
                    {
                        "type": "culture_planning",
                        "kor_type": "문화기획",
                        "count": culture_culture_planning_open_20_cnt
                    },
                    {
                        "type": "karaoke",
                        "kor_type": "노래방",
                        "count": culture_karaoke_open_20_cnt
                    },
                    {
                        "type": "video",
                        "kor_type": "비디오",
                        "count": culture_video_open_20_cnt
                    },
                    {
                        "type": "accommodation",
                        "kor_type": "숙박",
                        "count": culture_accommodation_open_20_cnt
                    },
                    {
                        "type": "travel",
                        "kor_type": "여행",
                        "count": culture_travel_open_20_cnt
                    },
                    {
                        "type": "movie",
                        "kor_type": "영화",
                        "count": culture_movie_open_20_cnt
                    },
                    {
                        "type": "music",
                        "kor_type": "음악",
                        "count": culture_music_open_20_cnt
                    }
                ]
            },
            {
                "category": "environment",
                "kor_type": "자연환경",
                "type_list": [
                    {
                        "type": "wood",
                        "kor_type": "목재",
                        "count": environment_wood_open_20_cnt
                    },
                    {
                        "type": "energy",
                        "kor_type": "에너지",
                        "count": environment_energy_open_20_cnt
                    },
                    {
                        "type": "groundwater",
                        "kor_type": "지하수",
                        "count": environment_groundwater_open_20_cnt
                    },
                    {
                        "type": "environment_management",
                        "kor_type": "환경관리",
                        "count": environment_environment_management_open_20_cnt
                    }
                ]
            },
            {
                "category": "food",
                "kor_type": "식품",
                "type_list": [
                    {
                        "type": "food",
                        "kor_type": "급식",
                        "count": food_school_meals_open_20_cnt
                    },
                    {
                        "type": "food",
                        "kor_type": "식품 제조/가공/판매",
                        "count": food_food_open_20_cnt
                    },
                    {
                        "type": "entertainment_bar",
                        "kor_type": "유흥주점/단란주점",
                        "count": food_entertainment_bar_open_20_cnt
                    },
                    {
                        "type": "restaurant",
                        "kor_type": "음식점",
                        "count": food_restaurant_open_20_cnt
                    }
                ]
            },
            {
                "category": "health",
                "kor_type": "건강",
                "type_list": [
                    {
                        "type": "healthcare_facility",
                        "kor_type": "의료기관",
                        "count": health_healthcare_facility_open_20_cnt
                    },
                    {
                        "type": "medical_appliances",
                        "kor_type": "의료기기",
                        "count": health_medical_appliances_open_20_cnt
                    }
                ]
            },
            {
                "category": "life",
                "kor_type": "생활",
                "type_list": [
                    {
                        "type": "salon",
                        "kor_type": "미용/이용",
                        "count": life_salon_open_20_cnt
                    },
                    {
                        "type": "laundry",
                        "kor_type": "세탁소/빨래방",
                        "count": life_laundry_open_20_cnt
                    },
                    {
                        "type": "distribution",
                        "kor_type": "유통",
                        "count": life_distribution_open_20_cnt
                    },
                    {
                        "type": "physical_education",
                        "kor_type": "체육",
                        "count": life_physical_education_open_20_cnt
                    },
                    {
                        "type": "bathhouse",
                        "kor_type": "목욕탕/찜질방/사우나",
                        "count": life_bathhouse_open_20_cnt
                    }
                ]
            },
            {
                "category": "other",
                "kor_type": "기타",
                "type_list": [
                    {
                        "type": "media",
                        "kor_type": "미디어",
                        "count": other_media_open_20_cnt
                    },
                    {
                        "type": "cigarette",
                        "kor_type": "담배",
                        "count": other_cigarette_open_20_cnt
                    },
                    {
                        "type": "logistics",
                        "kor_type": "물류",
                        "count": other_logistics_open_20_cnt
                    },
                    {
                        "type": "civil_defense",
                        "kor_type": "민방위",
                        "count": other_civil_defense_open_20_cnt
                    },
                    {
                        "type": "funeral",
                        "kor_type": "상조",
                        "count": other_funeral_open_20_cnt
                    },
                    {
                        "type": "elevator",
                        "kor_type": "엘리베이터",
                        "count": other_elevator_open_20_cnt
                    },
                    {
                        "type": "educational_institutions",
                        "kor_type": "전문교육기관",
                        "count": other_educational_institutions_open_20_cnt
                    },
                    {
                        "type": "office_support",
                        "kor_type": "사무지원",
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
