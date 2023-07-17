library(ggplot2)
library(dplyr)
library(readr)
library(tidyverse)

#import csv
benchmark <- read.csv("Benchmark.csv", header = TRUE)
tweets <- read.csv("BitcoinGPT.csv", header = TRUE)

#Preview
glimpse(tweets)
glimpse(benchmark)

#check the benchmark
ggplot(data = benchmark,
       mapping = aes(
         x = Flesch_Kincaid_Grade_Level,
         y = GPT_Score)) +
  geom_point()+
  geom_jitter(height=5)+
  geom_smooth(method = lm, formula = y ~ x, se = TRUE)+
  labs(title = "GPT vs CLEAR Corpus", subtitle = "Benchmarking GPT3.5's ability in Flesch-Kincaid text analysis.")
  
#check the correlation
correlation <- cor(benchmark$Flesch_Kincaid_Grade_Level, benchmark$GPT_Score)
print(correlation)

#cleaning the tweets into a data frame to remove missing values and irrelevant data
df <- data.frame(tweets$user_verified, tweets$GPT_Score)

#plot scores against counting for 
ggplot(df, aes(fill = tweets.user_verified, x = tweets.GPT_Score)) +
  geom_histogram(binwidth = 5, position = "dodge") +
  labs(title = "GPT score frequency compared to user verification", x = "GPT Score", y = "Count") +
  scale_fill_manual(name = "User Verified", values = c("black", "blue")) +
  coord_cartesian(ylim = c(NA, 350))+
  coord_cartesian(xlim = c(NA, 120))

#Average scores
average_scores <- aggregate(tweets.GPT_Score ~ tweets.user_verified, data = df, FUN = mean)
print(average_scores)

#Median scores
median_scores <- aggregate(tweets.GPT_Score ~ tweets.user_verified, data = df, FUN = median)
print(median_scores)