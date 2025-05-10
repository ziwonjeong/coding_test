# (done) codeup 2001: 최소 대금 https://www.codeup.kr/problem.php?id=2001

pasta, juice = [], []
for cnt in range(5):
    if cnt < 3:
        pasta.append(int(input()))
    else:
        juice.append(int(input()))
        

payment = (min(pasta) + min(juice)) * 1.1
print(f"{payment:.1f}")
    