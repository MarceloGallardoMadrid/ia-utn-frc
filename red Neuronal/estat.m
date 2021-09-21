function [prom va]=estat(x)
% calculo de la media muestral y la varianza muestral
n=length(x); s1=0; s2=0;
for i=1:n
s1=s1+x(i);
s2=s2+x(i)^2;
end
prom=s1/n;
va=(1/(n-1))*(s2-n*prom^2);