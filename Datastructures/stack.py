browser_session = []
browser_session.append(1)
browser_session.append(2)
browser_session.append(3)
#removing the last item LIFO
browser_session.pop()
print(browser_session)
print(browser_session[-1])
browser_session.pop()
print(browser_session)
browser_session.pop()
print(browser_session)
#if there is no button we have in the browser then to disable the back button
if not browser_session:
    print("the button is disable")



browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
browsing_session.pop()
print(browsing_session)
browsing_session.pop(0)
print(browsing_session)
browsing_session.pop()
if not browsing_session:
    print("you have nothing inside this list sir")




