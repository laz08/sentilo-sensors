library(ggplot2)
library(zoo)

dataframe<-read.csv(file="sensordataframeata.csv", header=TRUE, sep=",")
dataframe$rollmean<-mean(dataframe$value)


q<-ggplot(dataframe,aes(x=date, y=value, group=1)) +
  geom_point(aes(y=value,colour="dB(A)")) +
  geom_line(aes(y=rollmean,colour="Average")) + theme_classic() +
  theme(legend.title=element_blank(),legend.position="bottom") +
  labs(title="Noise in Pg. de Gracia",
        subtitle="In 11th of Sept., 2017",
       x="Hours",y="Noise") +
       scale_colour_manual(values=c("red","steelblue")
       )

q + theme(axis.text.x = element_text(angle = 90, hjust = 1))



ggsave("noise.png", height=4, width=10, dpi=120, type="cairo-png")
