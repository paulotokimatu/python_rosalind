A = 20
h = 30
a = 28

n=float(A+h+a)

# Calculate the probability of getting no dominant allelle
result = 1 - (h*a + 0.25*h*(h-1) + a*(a-1)) / (n*(n-1))

print result
