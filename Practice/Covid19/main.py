#!/usr/src/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def part_1(data):
    """
    1. Write a Python program to display first 5 rows from COVID-19 dataset. 
    Also print the dataset information and check the missing values.
    """
    # Print first 5 rows of dataset
    print(data[:][:5])
    
    # Prints info about dataset and column types...etc.
    print(data.info())

    # Prints N/A count for each column
    print(data.isna().sum())


def part_2(data):
    """
    2. Write a Python program to get the latest number of confirmed, deaths, 
    recovered and active cases of Novel Coronavirus (COVID-19) Country wise.
    """
    # Creates new column, active, which is the sum of active cases for each row
    data["Active"] = data["Confirmed"] - data["Deaths"] - data["Recovered"]
    
    # Groups rows by their Country/Region and displays the grouped sum of 
    # each of the shown fields
    # NOTE: reset_index() removes original indices and reindexes starting from 0
    result = data.groupby("Country_Region")["Confirmed", "Deaths", "Recovered", "Active"].sum().reset_index()
    print(result)


def part_3(data):
    """
    3. Write a Python program to get the latest number of confirmed deaths and
    recovered people of Novel Coronavirus (COVID-19) cases Country/Region - 
    Province/State wise.
    """
    # Groups buy Country/Region then Province/State and shows confirmed and recovered counts
    result = data.groupby(["Country_Region", "Province_State"])["Confirmed", "Deaths", "Recovered"].max()
    pd.set_option('display.max_rows', None)
    print(result)


def part_4(data):
    """
    4. Write a Python program to get the Chinese province wise cases of 
    confirmed, deaths and recovered cases of Novel Coronavirus (COVID-19).
    """
    # Data rows only where Country/Region is China
    """
    NOTE:
    data["Country_Region"]=="China" creates a mask of boolean values
    """
    result = data[data["Country_Region"]=="China"]
    # Shows the following columns
    result = result[["Province_State", "Confirmed", "Deaths", "Recovered"]]
    # Sorts results by confirmed cases
    result = result.sort_values(by="Confirmed", ascending=False)
    result = result.reset_index(drop=True)
    print(result)


def part_5(data):
    """
    5. Write a Python program to get the latest country wise deaths cases of 
    Novel Coronavirus (COVID-19).
    """
    # Groups by country/region and sums confirmed deaths and recovered in their
    # respective column
    result = data.groupby("Country_Region")["Confirmed","Deaths","Recovered"].sum().reset_index()
    # Masks only countries with more than 0 deaths
    result = result[result["Deaths"]>0][["Country_Region", "Deaths"]]
    print(result)


def part_6(data):
    """
    6. Write a Python program to list countries with no cases of Novel Coronavirus (COVID-19) recovered. 
    """

    result = data.groupby("Country_Region")["Confirmed", "Deaths", "Recovered"].sum().reset_index()
    result = result[result["Recovered"]==0][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    print(result)


def part_7(data):
    """
    7. Write a Python program to list countries with all cases of Novel
    Coronavirus (COVID-19) died.
    """
    result = data.groupby("Country_Region")["Confirmed", "Deaths", "Recovered"].sum().reset_index()
    result = result[result["Deaths"]>0][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    print(result)


def part_8(data):
    """
    Write a Python program to list countries with all cases of Novel Coronavirus
    (COVID-19) recovered.
    """
    result = data.groupby("Country_Region")["Confirmed", "Deaths", "Recovered"].sum().reset_index()
    result = result[result["Recovered"]>0][['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    print(result)


def part_10(data):
    """
    10. Write a Python program to create a plot (lines) of total deaths, 
    confirmed, recovered and active cases Country wise where deaths greater 
    than 150.
    """
    data["Active"] = data["Confirmed"] - data["Deaths"] - data["Recovered"]
    results = data.groupby("Country_Region")["Deaths", "Confirmed", "Recovered", "Active"].sum().reset_index()
    results = results.sort_values(by="Deaths", ascending=False)

    plt.figure(figsize=(15,5))
    min_val = 10000
    x_axis = results[results["Deaths"]>min_val]["Country_Region"]
    plt.plot(x_axis,results[results["Deaths"]>min_val]["Deaths"])
    plt.plot(x_axis,results[results["Deaths"]>min_val]["Confirmed"])
    plt.plot(x_axis,results[results["Deaths"]>min_val]["Recovered"])
    plt.plot(x_axis,results[results["Deaths"]>min_val]["Active"])
    plt.title("Countries with over 10k deaths")
    plt.show()


def part_11(data):
    """
    11. Write a Python program to visualize the state/province wise death 
    cases of Novel Coronavirus (COVID-19) in USA.
    """
    country_mask = data["Country_Region"]=="US"
    death_mask = data["Deaths"]>1000
    mask = country_mask & death_mask
    results = data[mask][["Province_State", "Deaths"]].reset_index()
    x_axis = results["Province_State"]
    print(x_axis)
    plt.bar(x_axis, results["Deaths"])
    plt.show()


def part_12(data):
    """
    12. Write a Python program to visualize the state/province wise active 
    cases of Novel Coronavirus (COVID-19) in USA.
    """
    country_mask = data["Country_Region"]=="US"
    data["Active"] = data["Confirmed"] - data["Deaths"] - data["Recovered"]
    death_mask = data["Active"]>4000
    mask = country_mask & death_mask
    results = data[mask][["Province_State", "Active"]].reset_index()
    x_axis = results["Province_State"]
    print(x_axis)
    plt.bar(x_axis, results["Active"])
    plt.show()    


def part_14(data):
    """
    13. Write a Python program to visualize the state/province wise combine 
    number of confirmed, deaths, recovered, active Novel Coronavirus (COVID-19) cases in USA.
    """


def main():
    data = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/07-26-2020.csv")
    
    # part_1(data)
    # part_2(data)
    # part_3(data)
    # part_4(data)
    # part_5(data)
    # part_6(data)
    # part_7(data)
    # part_10(data)
    # part_11(data)
    # part_12(data)

if __name__=="__main__":
    main()