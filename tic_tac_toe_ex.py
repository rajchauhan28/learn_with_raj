board=[0,1,2,3,4,5,6,7,8]
x=[1,3,5,9]
y=[2,4,6,8]
print("Enter name of user playing as 'x' player")
usrx = input()
print("Enter name of user playing as 'y' player")
usry = input()
def boards():
	print(board[0],"  l  ",board[1]," l  ",board[2])
	print("-------------------")
	print(board[3],"  l  ",board[4]," l  ",board[5])
	print("-------------------")
	print(board[6],"  l  ",board[7]," l  ",board[8])
boards()
print("The first move will be of",usrx," 'x'(cross) move and next will be of",usry," '0'(zero) ")
print("Every box contains a number so enter the number of the box which you want to make your move.")
try:
	for moves in range(15):
		print("enter the number")
		num=int(input())
		if board[num] != 'x' or board[num] != 'o':
			if moves in x:
				board[num]='x'
				boards()
			if moves in y:
				board[num]='o'
				boards()
		elif board[num] == 'x' or board[number] == 'o':
			print("this is already taken")
		elif board[0,4,8]=='x' or board[2,4,6]=='x' or board[0,3,6]=='x' or board[1,4,7]=='x' or board[2,5,8]=='x' :
			print('The',usrx,'is the winner')
		elif board[0,4,8]=='o' or board[2,4,6]=='o' or board[0,3,6]=='o' or board[1,4,7]=='o' or board[2,5,8]=='o':
			print('The',usry,'is the winner')
except ValueError:
	print('Invalid please try again')
	try:
		for moves in range(15):
			print("enter the number")
			num=int(input())
			if board[num] != 'x' or board[num] != 'o':
				if moves in x:
					board[num]='x'
					boards()
				if moves in y:
					board[num]='o'
					boards()
			elif board[num] == 'x' or board[number] == 'o':
				print("this is already taken")
			elif board[0,4,8]=='x' or board[2,4,6]=='x' or board[0,3,6]=='x' or board[1,4,7]=='x' or board[2,5,8]=='x' :
				print('The',usrx,'is the winner')
			elif board[0,4,8]=='o' or board[2,4,6]=='o' or board[0,3,6]=='o' or board[1,4,7]=='o' or board[2,5,8]=='o':
				print('The',usry,'is the winner')
