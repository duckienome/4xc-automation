from rich.style import Style

'''Defines Color pallats for styling'''
colors = {
    "neutral" : Style(color="dark_orange"),
    "input" : Style(color="cyan"),
    "warn" : Style(color="bright_yellow"),
    "error" : Style(color="red1"),
    "success" : Style(color="green1",italic=True)        
}


'''Defines Spinner style'''
spinner = {
    "style" : "bouncingBar"
}
