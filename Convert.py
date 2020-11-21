class Solution:
	def romanToInt(self, s:str)->int:
		try:
			s = s.replace(' ','')
			if 1>=len(s) and 15<=len(s):
				return None

			Rims = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
			numbers = []

			for symbol, value in Rims.items():
				s = str(s)
				s = s.replace(symbol,str(value)+',')
			strs = s.split(',')
			strs.pop()

			numbers = [int(item) for item in strs]

			Sum = 0
			for i in range(0,len(numbers)-1):
				if numbers[i] >= numbers[i+1]:
					Sum +=numbers[i]
				elif numbers[i] < numbers[i+1]:
					Sum -=numbers[i]
			Sum+= numbers[len(numbers)-1]

		except: 
			return None
		return Sum
