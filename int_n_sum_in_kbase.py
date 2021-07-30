class Solution(object):
    def sum_kbase(self, n: int, k:int) -> int:
        sum_list= []
        a = n
        while a > 0:
            sum_list.append(a%k)
            a //= k
        return sum(sum_list), int(''.join(list(map(str,sum_list[::-1]))))

n = int(input("Insert a base 10 number: "))
k = int(input("Insert the desired base for conversion: "))
z = Solution()
print(f'The integer {n} in base {k} is equal to: {z.sum_kbase(n,k)[1]}\nThe sum of its digits is: {z.sum_kbase(n,k)[0]}')









