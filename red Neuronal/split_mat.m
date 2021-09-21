function [x y]=split_mat(mat)  r=rows(mat);  c=columns(mat);  x=[];  y=[];  for i=1:r*c    if(i<=r)      x=[x mat(i)];    else      y=[y mat(i)];    endif  endfor
endfunction