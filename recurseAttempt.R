rec = function(i, vec)
{
  if (i < length(vec))
  {
    for (j in (i+1):length(vec))
    {
      cat(vec[i], ",", vec[j], "\n")
      rec(j, vec)
    }
  }
}

rec(1, vec)


for (i in 1:(length(vec)-1))
  for (j in (i+1):length(vec))
    cat(vec[i], ",", vec[j], "\n")




vec = c(1,2,3,4)
subset = function(vec)
{
  cat(vec, ", ")
  if (length(vec) > 1)
  {
    for (i in 1:length(vec))
      subset(vec[-i])
  }
}
subset(vec)




