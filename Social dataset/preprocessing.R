# Map 1-based optional input ports to variables
data <- data <- read.csv('student-por.csv', sep=";",header=TRUE) # class: data.frame

# delete observations with score 0
data <- subset(data, data$G3>=1)

# create vectors for categorical, multi-categorical and numeric data
cat_data <- c("school","sex","address","famsize","Pstatus","schoolsup","famsup",
"paid","activities", "nursery","higher", "internet","romantic")

multi_cat <- c("Mjob","Fjob","reason","guardian")

numeric_data <-  c("age","Medu","Fedu","traveltime","studytime",
"famrel","freetime","goout","Dalc","Walc","health","absences",
"failures","G2","G1","G3")

# transform multi categoricals
for(i in multi_cat) {
for(level in unique(data[,i])){
data[paste(paste("bin",i,sep="_"), level, sep = "_")] <- ifelse(data[,i] == level, "yes", "no")
}
}

# select dummy variables
new_multi_cat <- grep("bin_",colnames(data))
new_multi_cat <- names(data)[new_multi_cat]

# make them factors
for (i in new_multi_cat) {
data[,i] <- as.factor(data[,i])
}

# create a new dataset based on prior categorical, new binary, and numeric data
select <- c(cat_data, new_multi_cat, numeric_data)
data <- data[,select]

# calculate pass/fail
data$result <- as.factor(sapply(data$G3,function(res)
if (res >=10) 'pass' else 'fail'))

# Select data.frame to be sent to the output Dataset port
write.csv(data, 'processedData.csv');