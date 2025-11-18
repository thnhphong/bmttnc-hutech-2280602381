print("Enter srting (Enter 'done' to stop):");
lines = [];
while True:
    line = input();
    if line.lower() == 'done':
        break;
    lines.append(line);

print("\nUppercased string:");
for line in lines:
    print(line.upper());