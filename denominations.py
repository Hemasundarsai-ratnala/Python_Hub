amount=int(input())
fhn=amount//500
rem_bal=amount%500
print("Five Hundred Notes (500): ",fhn)
hn=rem_bal//100
rem_bal=rem_bal%100
print("Hundred Notes (100):",hn)
fn=rem_bal//50
rem_bal=rem_bal%50
print("Fifty Notes (50):",fn)
tn=rem_bal//10
rem_bal=rem_bal%10
print("Ten Notes (10):",tn)

