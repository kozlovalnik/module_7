team1_num = 5
print("В команде Мастера кода участников: %s !" % team1_num)
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

score_1, score_2 = 42, 40
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team1_time = 18015.2
team2_time = 18015.3
print("Волшебники данных решили задачи за {} с !".format(team1_time))

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
tasks_total = 82
time_avg = round((team1_time + team2_time) / 82, 2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
