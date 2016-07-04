library(shiny)

shinyUI(fluidPage(
  titlePanel("Države"),
  sidebarLayout(
    sidebarPanel(
            sliderInput("max_kcal",
                        "Max stevilo kalorij:",
                        min = 0,
                        max = 900,
                        value = 10)
          ),
      
      mainPanel(
  tableOutput("plezalisca")
    
  ))))