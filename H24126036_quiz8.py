import csv

# read CSV 文件
with open("/Users/Downloads/nba_standings.csv", 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 先將勝負的次數用-分隔取出來，然後算勝負率
def win_loss_percentage(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)
eastern_teams_lower_home_pct = []
for row in data:
    if row['Conference'] == 'Eastern':
        home_pct = win_loss_percentage(row['Home'])
        away_pct = win_loss_percentage(row['Away'])
        if home_pct < away_pct:
            eastern_teams_lower_home_pct.append(row['Team'])

print("Eastern Conference teams with Home win-loss percentage lower than Away:", eastern_teams_lower_home_pct)

# Question 2: 
conference_scores = {'Eastern': [], 'Western': []}
for row in data:
    pf_minus_pa = int(row['PF']) - int(row['PA'])
    conference_scores[row['Conference']].append(pf_minus_pa)

#計算平均得分減掉失分,取最大值
average_pf_pa_diff = {conf: sum(scores)/len(scores) for conf, scores in conference_scores.items()}
higher_avg_diff_conference = max(average_pf_pa_diff, key=average_pf_pa_diff.get)
print("Conference with higher average difference of 'PF minus PA':", higher_avg_diff_conference)

# Question 3: 
# 假設 CSV 有一列叫做 'Interconference_W' ，表示對另一區的勝場數

if 'Interconference_W' in data[0]:
    data.sort(key=lambda x: int(x['Interconference_W']), reverse=True)
    ranking_list = [(row['Team'], int(row['Interconference_W'])) for row in data]
    print("Ranking list of all teams based on wins against the other conference's teams:")
    for rank, (team, interconference_wins) in enumerate(ranking_list, start=1):
        print(f"{rank}. {team} - {interconference_wins} wins")
else:
    print("CSV does not contain 'Interconference_W' column for ranking based on interconference wins.")
