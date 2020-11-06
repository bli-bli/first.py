# with as 를 사용할 경우 따로 close 를 해줄 필요가 없다
import pickle
with open("profile.pickle", "rb") as profile_file:
            print(pickle.load(profile_file))


