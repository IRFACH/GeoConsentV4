print("""
Choose link type:

1) GPS only
2) Camera only
3) GPS + Camera
""")

choice = input("Enter choice (1/2/3): ")

base = "https://YOUR-CLOUDFLARE-URL.trycloudflare.com/share"

if choice == "1":
    print(base + "?mode=gps")
elif choice == "2":
    print(base + "?mode=camera")
elif choice == "3":
    print(base + "?mode=both")
else:
    print("Invalid choice")
