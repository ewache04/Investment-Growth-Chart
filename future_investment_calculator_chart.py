'''
Author name: Jeremiah E. Ochepo
Last Edited: 2/15/2020 (7 PM)
Description: Investment Growth Chart
'''

from graphics import *


def my_investment_growth():
    # Introduction
    print("This program plots the growth of a 10-year investment.")

    # Get principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: ")) / 100
    numb_years = int(input("Enter the number of years: "))

    # Create a graphics window with labels on the left edge
    win = GraphWin('Investment Growth Chart', 400, 400)
    win.setBackground('white')

    # Draw labels on the left edge
    labels = ['10.0K', '7.5K', '5.0K', '2.5K', '0.0K']
    for i in range(5):
        Text(Point(20, 30 + i * 50), labels[i]).draw(win)

    # Draw bar for initial principal
    initial_height = principal * 0.02
    initial_bar = Rectangle(Point(40, 230), Point(65, 230 - initial_height))
    initial_bar.setFill('green')
    initial_bar.setWidth(2)
    initial_bar.draw(win)

    # Draw bars for successive years
    for year in range(1, numb_years + 1):
        # Calculate value for the next year
        principal *= (1 + apr)

        # Draw bar for this value
        x_ll = year * 25 + 40
        height = principal * 0.02

        bar = Rectangle(Point(x_ll, 230), Point(x_ll + 25, 230 - height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

        print(f'Year #{year}: {round(principal, 2)}')

    # Close the graphics window when Enter is pressed
    input('Press <Enter> to quit')
    win.close()


if __name__ == "__main__":
    my_investment_growth()
