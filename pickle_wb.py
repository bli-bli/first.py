# 프로그램에서 사용하고 있는 데이터를 파일의 형태로 저장
# pickle 에서는 항상 binary 타입을 지정해주어야하며 인코딩 설정을 따로 해줄 필요가 없다
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이": 30, "취미":["골프", "영화보기"]}

# profile 에 있는 정보를 pickle 을 이용해서 profile_file 에 저장
pickle.dump(profile, profile_file)
profile_file.close()
