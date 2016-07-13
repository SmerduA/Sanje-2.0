library(shiny)

shinyUI(fluidPage(
  titlePanel("Plezališča"),
  
  tabsetPanel(
    
  #############################
    
  tabPanel( "Plezališča po državah",
    sidebarLayout(
    sidebarPanel(
      selectInput("izberi_drzavo",
                  label = "Izberi državo:",
                  choices = list("vse države", "Avstrija","Bosna in Hercegovina","Češka","Črna gora","Grčija","Hrvaška", "Juzna Afrika", "Maroko", "Nemčija", "Poljska", "Slovaška", "Slovenija","Španija", "Srbija", "Švedska", "Švica", "Tajska", "Turčija" ,"Združene države Amerike"),
                  selected="vse države"
    ),
    sliderInput("stevilo_smeri",
                label= "Število smeri v plezališču:",
                min= 1,
                max =706,
                value=c(1, 706)
      
    )
    ),
    
    mainPanel(
  tableOutput("plezaliscaPoDrzavah")
))),
##############################
tabPanel( "Države",
          sidebarLayout(
            sidebarPanel(
              sliderInput("st_plezalisc",
                          label = "Število plezališč:",
                          min = 1,
                          max = 103,
                          value = c(0,103)
              )),
            
            mainPanel(
              tableOutput("drzavestevilo")
            ))),

##############################
tabPanel( "Države glede na število plezališč",
          sidebarLayout(
            sidebarPanel(
              selectInput("nacinprikaza",
                          label = "Izberi način prikaza:",
                          choices=list("histogram", "tortni diagram")
              )
              
              ),
            
            mainPanel(
              plotOutput("drzavetorta")
            ))),
##############################

tabPanel( "Poišči plezališče po meri",
          sidebarLayout(
            sidebarPanel(
              selectInput("ppdrzava", label="Izberi državo:",
                          choices = list("vse države", "Avstrija","Bosna in Hercegovina","Češka","Črna gora","Grčija","Hrvaška", "Juzna Afrika", "Maroko", "Nemčija", "Poljska", "Slovaška", "Slovenija","Španija", "Srbija", "Švedska", "Švica", "Tajska", "Turčija" ,"Združene države Amerike"),
                          selected = "vse države"),


              numericInput("mindolzina",
                          label="Izberi minimalno dolžino smeri (m)",
                          value = 0,
                          min= 0,
                          max = 680
              ),
              numericInput("maxdolzina",
                           label="Izberi maksimalno dolžino smeri (m)",
                           value = 680,
                           min= 0,
                           max = 680
              ),
              numericInput("maxtezavnost",
                           label="Izberi maksimalno težavnost smeri",
                           value = 6,
                           min= 1,
                           max = 9
              ),
              numericInput("mintezavnost",
                           label="Izberi minimalno težavnost smeri",
                           value = 1,
                           min= 1,
                           max = 9
              )
            #   sliderInput("ppdolĹľina",
            #               label="Izberi dolĹľino smeri",
            #               min= 0,
            #               max = 680,
            #               value=c(0, 680)
            #   ),
            # sliderInput("ppsmeri",
            #             label = "Izberi Ĺˇtevilo smeri z doloÄŤeno dolĹľino in teĹľavnostjo",
            #             min= 1,
            #             max =706,
            #             value=c(1, 706)
           ),
             mainPanel( tableOutput("ppplezalisca")
               
             ))),
###################################
tabPanel( "Nekaj grafov",
          sidebarLayout(
            sidebarPanel(
              selectInput("ddrzava",
                          label = "Izberi državo:",
                          choices = list("vse države", "Avstrija","Bosna in Hercegovina","Češka","Črna gora","Grčija","Hrvaška", "Juzna Afrika", "Maroko", "Nemčija", "Poljska", "Slovaška", "Slovenija","Španija", "Srbija", "Švedska", "Švica", "Tajska", "Turčija" ,"Združene države Amerike"),
                          selected="vse države"
              ),
              selectInput("ddoltez",
                          label = "Izberi, kaj te zanima:",
                          choices = list("dolžina smeri", "težavnost smeri"),
                          selected="dolžina smeri"
              )
                          
              
            ),
            
            mainPanel(
              plotOutput("grafi")
            )))

  )))