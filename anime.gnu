set terminal gif animate delay 1 optimize size 640,480
set output "pendulum.gif"
do for [i=0: 99] {
  plot [-2:2] [-2:2] "coordinate.dat" index i with line
}
unset output