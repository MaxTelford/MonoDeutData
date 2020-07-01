library(ggtern)
library(plyr)



points<- data.frame(
  rbind(c( 1,1,0,0),
        c( 2,0.66666,0,0.33333),
        c( 3,0.66666,0.33333,0),
        c( 4,0,1,0),
        c( 5,0.33333,0.66666,0),
        c( 6,0,0.66666,0.33333),
        c( 7,0,0,1),
        c( 8,0,0.33333,0.66666),
        c( 9,0.33333,0,0.66666),
        c(10,0.16666,0.16666,0.66666),
        c(11,0.66666,0.16666,0.16666),
        c(12,0.16666,0.66666,0.16666)
  )
)

colnames(points) = c("IDPoint","L","T","R")

laumer <- read.csv("Laumer_AllLikelihoodsScores.csv", header=TRUE)
laumer$Study <- "Laumer"
marletaz <- read.csv("Marletaz_AllLikelihoodsScores.csv", header=TRUE)
marletaz$Study <- "Marletaz"
cannon <- read.csv("Cannon_AllLikelihoodsScores.csv", header=TRUE)
cannon$Study <- "Cannon"
rouse <- read.csv("Rouse_AllLikelihoodsScores.csv", header=TRUE)
rouse$Study <- "Rouse"
telford <- read.csv("Telford_AllLikelihoodsScores.csv", header=TRUE)
telford$Study <- "Telford"

all <- rbind(laumer,marletaz,cannon,marletaz,telford)

polygon.labels<- data.frame(
  Label=c("T1",
          "T13",
          "T3",
          "T23",
          "T2",
          "T12",
          "T123"
  ))

#Assign each label an index
polygon.labels$IDLabel=1:nrow(polygon.labels)

#Create a map of polygons to points
polygons <- data.frame(
  rbind(c(1,1),c(1,2),c(1,3),
        c(2,3),c(2,11),c(2,12),c(2,5),
        c(3,5),c(3,4),c(3,6),
        c(4,6),c(4,12),c(4,10),c(4,8),
        c(5,8),c(5,7),c(5,9),
        c(6,9),c(6,10),c(6,11),c(6,2),
        c(7,11),c(7,12),c(7,10) )
)
#IMPORTANT FOR CORRECT ORDERING.
polygons$PointOrder <- 1:nrow(polygons)

#Rename the columns
colnames(polygons) = c("IDLabel","IDPoint","PointOrder")

#Merge the three sets together to create a master set.
df <- merge(polygons,points)
df <- merge(df,polygon.labels)
df <- df[order(df$PointOrder),]

#Determine the Labels Data library(plyr)
Labs = ddply(df,"Label",function(x){c(c(mean(x$T),mean(x$L),mean(x$R)))})
colnames(Labs) = c("Label","T","L","R")


pch = 21  


L_prot <- "#d40000"
R_prot <- "#de8787"
Top_prot <- "#aa4400"

L_deut <- "#1f78b4"
R_deut <- "#2ca089"
Top_deut <- "#6a51a3"

LR <- "light grey"
LT <- "light grey"
TR <- "light grey"
LTR <- "grey"

c("#312058", "#2d276f", "#2d3886", "#32589f", 
  "#377eb8", "#4289c2", "#4e93cd", "#5b9fd5",
  "#69a9dd", "#77b4e4", "#86bfeb", "#97c9f0",
  "#a8d3f5", "#baddf9", "#cce7fb")


c("#413805", "#533604", "#652d04", "#781b02", 
  "#8b0000", "#981010", "#a32121", "#af3131", 
  "#ba4141", "#c35252", "#cc6262", "#d47272",
  "#dc8383", "#e39393", "#e9a3a3")

c("#720d10", "#7d0e11", "#891013", "#941114", 
  "#a01215", "#ab1417", "#b61517", "#c21619",
  "#cd171a", "#d9191b", "#e41a1c", "#ec2c2d", 
  "#f33e3f", "#f95254", "#fd6868", "#ff8080", 
  "#ff9999", "#ffb3b3", "#ffcccc", "#ffe6e6", 
  "#ffffff")

my_named_vector_prot = c(
  "T1" = "black",
  "T2" = "black",
  "T3" = "black",
  "T12"  = "black",
  "T23" = "black",
  "T13" = "black",
  "T123" = "black")

my_named_vector_deut = c(
  "T1" = "black",
  "T2" = "black",
  "T3" = "black",
  "T12"  = "black",
  "T23" = "black",
  "T13" = "black",
  "T123" = "black")

c("#80110e", "#911210", "#a21312", "#b31414", 
  "#c31616", "#d31819", "#e41a1c", "#e62d2f", 
  "#e83f42", "#eb5255", "#ed6468", "#ee777b", 
  "#f18a8d", "#f39c9f", "#f5afb2", "#f7c1c4")


ternary_prot <- ggtern(data=df, 
                  aes(L,T,R)) +
  geom_polygon(aes(fill=Label), color="black", alpha = 0.6) +
  geom_point(all, mapping = aes(all$L1_Prot, 
                                all$L3_Prot,
                                all$L2_Prot,
                                color=Class_Prot
             ),
             alpha=0.6,size = 0.2,
             #colour="dark grey",
             show.legend = FALSE
  )+
  theme_nolabels() +
  theme_nogrid() +
  scale_fill_manual(values = c(L_prot, LR, LTR, LT, R_prot, TR, Top_prot)) +
  scale_color_manual(values = my_named_vector_prot, na.translate = FALSE)

ternary_deut <- ggtern(data=df, 
                       aes(L,T,R)) +
  geom_polygon(aes(fill=Label), color="black") +
  geom_point(all, mapping = aes(all$L1_Deut, 
                                all$L3_Deut,
                                all$L2_Deut,
                                color=Class_Deut
  ),
  alpha=0.6, size = 0.2,
  #colour="dark grey",
  show.legend = FALSE
  )+

  theme_nolabels() +
  theme_nogrid() +
  scale_fill_manual(values = c(L_deut, LR, LTR, LT, R_deut, TR, Top_deut)) +
  scale_color_manual(values = my_named_vector_deut, na.translate = FALSE)



ternary_prot
ternary_deut
ggsave(filename="triangle_prot.svg", plot=ternary_prot, width=10, height=8)
ggsave(filename="triangle_deut.svg", plot=ternary_deut, width=10, height=8)