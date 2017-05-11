function plotvs(mc, namefile, T)

x=mc(1:1001,1)
y2=mc(1:1001,2)
y3=mc(1:1001,3)
y4=mc(1:1001,4)

hold on; plot(x(1:50:end), y2(1:50:end), 'k-s')
%hold on; plot(x(1:50:end), y3(1:50:end), 'k-.')
%hold on; plot(x(1:50:end), y4(1:50:end), 'k-o')

%legend('CRO','QIEA','QCRO', 'Location', 'best')

xlabel('No. of Iterations')
ylabel('Max Fitness')
title(T)

fig=gcf;
set(fig, 'PaperUnits', 'centimeters', 'PaperPosition', [0 0 15 6]);%
print(namefile, '-dpng', '-r0')