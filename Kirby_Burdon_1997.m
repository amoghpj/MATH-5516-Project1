clear all
close all

%%%%%%%%%%%%%%%FIGURE 1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
m=[0,1e-10,1e-6,1e-4];
for i = 1:4 
    output=KB_fig1(0.999,0.001,0.3,0,0.8,1,0.03,m(i),500);
    figure(1)
    subplot(2,2,i)
    plot(output(2,:),output(1,:),'k')
    xlim([0 1]), ylim([0 1])
    xlabel('Pathogen Virulence')
    ylabel('Host Susceptibility')
end
%
% 
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %%%%%%%%%%%%%%%FIGURE 1%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% 
% %%%%%%%%%%%%%%%FIGURE 2%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
%
m=[0,1e-4,1e-4,1e-10];
n=[0.9,0.001,0.9,0.001];
q=[0.9,0.999,0.9,0.999];
for i = 1:4 
    output=KB_fig2(q(i),n(i),0.3,0,0.8,1,0.03,m(i),500);
    figure(2)
    subplot(2,2,i)
    plot(output(2,:),output(1,:),'k')
    xlim([0 1]), ylim([0 1])
    xlabel('Pathogen Virulence')
    ylabel('Host Susceptibility')
end
% %
% %
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % %%%%%%%%%%%%%%%FIGURE 2%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %
% %
% % %%%%%%%%%%%%%%%FIGURE 3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% %
% %
% FIGURE 3A, 3B, 3C
m=[1e-4,1e-5,1e-6];
tmax=[200,400,200];
for i = 1:3 
    for j = 1:3
        output=KB_fig3(0.999,0.001,0.3,0,0.8,1,0.03,m(i),tmax(i));
        figure(3)
        subplot(2,2,i)
        plot(output(2,:),output(1,:))
        xlim([0 1]), ylim([0 1])
        xlabel('Pathogen Virulence')
        ylabel('Host Susceptibility')
        hold on
    end
end
%
%
%FIGURE 3D
for j = 1:3 
    output=KB_fig3(0.9625,0.83667,0.3,0,0.8,1,0.03,1e-5,500);
    figure(3)
    subplot(2,2,4)
    plot(output(2,400:501),output(1,400:501))
    xlim([0 1]), ylim([0 1])
    xlabel('Pathogen Virulence')
    ylabel('Host Susceptibility')
    hold on
end
% %
% %
% % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% % %%%%%%%%%%%%%%%FIGURE 3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%