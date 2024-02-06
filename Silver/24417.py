# 問題文をみるに求めた値を1000000007で割った余りを求める必要があるため使用する変数
mod = 10**9+7
# 入力
n = int(input())
# 入出力例からDPで求める場合の計算回数がn-2だとわかるためその値を格納
ans = n-2
# 再帰を使うとerrorになるためforで効率的に計算(これが思いつくかが肝)
x,y = 1,1 # ピボナッチの初期値
# ピボナッチ計算(初期値をセットしてあるため-2)。
for i in range(n-2):
    y,x = (x+y)%mod,y # やってることはいつものdp[i]=dp[i-1]+dp[i-2]と同じ
# 出力
print(y,ans)

"""
https://www.acmicpc.net/problem/24417
"""