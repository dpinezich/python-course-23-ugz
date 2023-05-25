def change(za, tx, li, di, st):
    za = 8
    tx = "ciao "
    li[0] = 7
    di["x"] = 7
    st.discard(3)
    print(f"Function: {za} {tx} {li} {di} {st}")
hza = 3
htx = "hello"
hli = [3,"abc"]
hdi = {"x":3, "y":"abc"}
hst = set([3, "abc"])
print(f"Before:   {hza} {htx} {hli} {hdi} {hst}")
change(hza, htx, hli, hdi, hst)
print(f"After:  {hza} {htx} {hli} {hdi} {hst}")