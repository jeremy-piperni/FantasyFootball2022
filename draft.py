import pandas as pd
import numpy as np

olpff=pd.read_excel("D://FantasyFootball2022/ol/ol-pff.xlsx")
olpff = olpff.groupby("TEAM_2021").mean()
olpff.rename(columns={"PFF_2021" : "OL_PFF_2021"},inplace=True)

df=pd.read_csv("D://FantasyFootball2022/FantasyPros_2022_Draft_ALL_Rankings.csv")
df["SOS SEASON"].replace(" out of 5 stars", "", regex=True, inplace=True)
df.drop(["ECR VS. ADP", "SOS SEASON"], axis=1, inplace=True)
df[["POS","POS_RANK"]] = df["POS"].str.extract("([A-Za-z]+)(\d+)")
df.rename(columns={"PLAYER NAME":"PLAYER_NAME", "BYE WEEK":"BYE_WEEK", "TEAM":"TEAM_2022", "RK":"RANK"},inplace=True)
df["TEAM_2022"].replace("HOU", "HST", regex=True, inplace=True)
df["TEAM_2022"].replace("BAL", "BLT", regex=True, inplace=True)
df["TEAM_2022"].replace("ARI", "ARZ", regex=True, inplace=True)
df["TEAM_2022"].replace("LAR", "LA", regex=True, inplace=True)
df["TEAM_2022"].replace("JAC", "JAX", regex=True, inplace=True)
df["TEAM_2022"].replace("CLE", "CLV", regex=True, inplace=True)
df = df[df.POS != "K"]
df["RANK"] = np.arange(1, len(df) + 1)


qb2021 = pd.read_csv("D://FantasyFootball2022/qb/qb-fantasy-2021-points.csv")
qb2020 = pd.read_csv("D://FantasyFootball2022/qb/qb-fantasy-2020-points.csv")
qb2019 = pd.read_csv("D://FantasyFootball2022/qb/qb-fantasy-2019-points.csv")
qb2021.rename(columns={"Name":"PLAYER_NAME", "Team":"TEAM_2021", "TOTAL":"PTS_2021"}, inplace=True)
qb2020.rename(columns={"Name":"PLAYER_NAME", "Team":"TEAM_2020", "TOTAL":"PTS_2020"}, inplace=True)
qb2019.rename(columns={"Name":"PLAYER_NAME", "Team":"TEAM_2019", "TOTAL":"PTS_2019"}, inplace=True)
qb2021.drop(["Ovr","W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12","W13","W14","W15","W16","W17","W18"], axis=1, inplace=True)
qb2020.drop(["Ovr","W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12","W13","W14","W15","W16","W17","W18"], axis=1, inplace=True)
qb2019.drop(["Ovr","W1","W2","W3","W4","W5","W6","W7","W8","W9","W10","W11","W12","W13","W14","W15","W16","W17","W18"], axis=1, inplace=True)
df = pd.merge(df, qb2021, how="left", on="PLAYER_NAME")
df = pd.merge(df, qb2020, how="left", on="PLAYER_NAME")
df = pd.merge(df, qb2019, how="left", on="PLAYER_NAME")
qbsos = pd.read_csv("D://FantasyFootball2022/qb/qb-fantasy-sos.csv")
qbsos = qbsos[["Offense","Season SOS"]]
qbsos.rename(columns={"Offense": "TEAM_2022", "Season SOS": "SOS_2022"}, inplace=True)
qbsos.sort_values(by=["SOS_2022"], inplace=True, ascending=False)
qbsos["SOS_RANK_2022"] = np.arange(1, len(qbsos) + 1)
print(qbsos)
df = pd.merge(df, qbsos, how="left", on="TEAM_2022")
qbpff = pd.read_csv("D://FantasyFootball2022/qb/qb-pff.csv")
df = pd.merge(df, qbpff, how="left", on="PLAYER_NAME")
df = pd.merge(df, olpff, how="left", on="TEAM_2021")
print(df[df["POS"]=="QB"])

