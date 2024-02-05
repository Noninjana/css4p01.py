#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:25:06 2024

@author: nyawuzakazi
"""

import pandas as pd

#Load the dataset
df = pd.read_csv("movie_dataset.csv")

#Inspect the Data
#print(df.info())

#Remove Index Column
#df.drop(['Index'],inplace=True,axis=1)

#Handle Columns with Spaces
df.columns = df.columns.str.replace(' ', '_')

#Handle Missing Values:
#df.dropna(inplace=True)
df['Metascore'].fillna(df['Metascore'].mean(), inplace=True)
df['Revenue_(Millions)'].fillna(df['Revenue_(Millions)'].mean(), inplace=True)


print(df.isna().any())

# Check the dataset after cleaning
#print("\nAfter cleaning:")
print(df.info())

# highest rated movie
highest_rated_movie_index = df['Rating'].idxmax()

# Display the data for the highest-rated movie
highest_rated_movie_data = df.loc[highest_rated_movie_index]
print("Data for the highest-rated movie:")
print(highest_rated_movie_data)

#Calculate Average Revenue of all the movies
average_revenue = df['Revenue_(Millions)'].mean()
print("Average Revenue of All Movies:", average_revenue)

# Filter movies released from 2015 to 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for movies released from 2015 to 2017
average_revenue_2015_to_2017 = filtered_df['Revenue_(Millions)'].mean()

print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_to_2017)

# Filter movies released in the year 2016
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies released in 2016
num_movies_2016 = len(movies_2016)

print("Number of Movies Released in 2016:", num_movies_2016)

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Count the number of movies directed by Christopher Nolan
num_nolan_movies = len(nolan_movies)

print("Number of Movies Directed by Christopher Nolan:", num_nolan_movies)

# Filter movies with a rating of at least 8.0
high_rated_movies = df[df['Rating'] >= 8.0]

# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = len(high_rated_movies)

print("Number of Movies with a Rating of at Least 8.0:", num_high_rated_movies)

# Filter movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)

# Group by release year and calculate the average rating for each year
average_rating_by_year = df.groupby(df['Year'])['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()

print("Year with the Highest Average Rating:", year_highest_average_rating)

# Filter movies released between 2006 and 2016
movies_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

# Count the number of movies released in each year
movie_count_2006 = len(df[df['Year'] == 2006])
movie_count_2016 = len(df[df['Year'] == 2016])

# Calculate the percentage increase
percentage_increase = ((movie_count_2016 - movie_count_2006) / movie_count_2006) * 100

print("Percentage Increase in Number of Movies between 2006 and 2016:", percentage_increase)

# Split the 'Actors' column to get individual actors
all_actors = df['Actors'].str.split(', ', expand=True).stack()

# Count the occurrences of each actor
most_common_actor = all_actors.value_counts().idxmax()

print("Most Common Actor in All Movies:", most_common_actor)

# Split the 'genres' column to get individual genres
all_genres = df['Genre'].str.split(', ', expand=True).stack()

# Count the number of unique genres
num_unique_genres = all_genres.nunique()

print("Number of Unique Genres in the Dataset:", num_unique_genres)

# Using numerical columns in the dataset
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix
correlation_matrix = numerical_features.corr()

# Correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
