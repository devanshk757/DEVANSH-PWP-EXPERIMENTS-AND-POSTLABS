from plotnine import *
from plotnine.data import mtcars
from plotnine.ggplot import ggplot


# print(mtcars.head())

# a = (ggplot(mtcars)
#  + geom_point(mapping=aes(x="wt", y="mpg", color="factor(gear)"))
#  + facet_wrap("~gear"))

# a = (ggplot(data=mtcars)
#  + geom_point(aes("wt", "mpg", color="factor(gear)"))
# )

# a = (ggplot(data=mtcars)
#  + geom_point(aes("wt", "mpg", size="factor(gear)"))
# )

# a = (ggplot(data=mtcars)
# + geom_point(aes("wt", "mpg"), color='red')
# )


#------------------------------------------------------------------POST-LAB------------------------------------------------------------------
#1.
# from plotnine.data import economics
# print(economics)

#2.
# from plotnine.data import economics
# from plotnine import ggplot, aes, geom_line

# (
#     ggplot(economics)  # What data to use
#     + aes(x="date", y="pop")  # What variable to use
#     + geom_line()  # Geometric object to use for drawing
# )

#3.
# from plotnine.data import mpg
# from plotnine import ggplot, aes, geom_point

# ggplot(mpg) + aes(x="class", y="hwy") + geom_point()

