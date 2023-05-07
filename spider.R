#spider plot for oncology studies
#with interactive feature tooltips

library(sas7bdat)
library(plotly)

# Read in the SAS data
adtr <- read.sas7bdat("adtr.sas7bdat")


library(shiny)
library(ggplot2)
data.frame(adtr)


tr <- adtr[(adtr$PARAMCD=='SUMDIAM' & adtr$COHORT=='Cohort 2' & adtr$PARQUAL=='CENTRAL' & adtr$TRACPTFL=='Y' & adtr$ANL01FL=='Y' & adtr$SUBJID != '81020005'),]

tr <- tr[c("ADY","PCHG","SUBJID")]


tr$x <- ifelse(tr$AVISITN==1, 0, tr$ADY/7)
tr$y <- ifelse(tr$AVISITN==1, 0, tr$PCHG)

data.frame(tr)

ui <- fluidPage( 
  
  mainPanel( plotlyOutput("spPlot") 
  ) 
) 

server <- function(input, output) {
  output$spPlot <- renderPlotly({ 
    myPlot <- ggplot(tr, aes(x = x, y = y, group=SUBJID)) + 
      labs(title = "Spider plot for percent change from baseline in tumor size", 
           x = "Treatment duration weeks", y = "Percent change from baseline(%)") +
      
      geom_line(size=1) +
      geom_point( size=2)
    print(myPlot) }) 
}


shinyApp(ui=ui, server=server)