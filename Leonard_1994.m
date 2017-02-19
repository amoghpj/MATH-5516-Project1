clear all
close all

%Initial Conditions
P(1) = 0.163; %FIgure 2A
N(1) = 0.2; %Figure 2A
%P(1) = 0.163; %FIgure 2B
%N(1) = 0.18; %Figure 2B


%Frequencies
p_freq=[];
n_freq=[];

%Parameters
k=0.3;
a=0.0;
t=1.0;
c=0.03;
s=0.8;

%Generations
tmax=165; %Figure 2A
%tmax=194; %Figure 2B

%Model
for x = 1:tmax
    q=1-P(x);
    N(x+1) = (N(x).*(1-k+(1-q.^2).*a))./(1-(1-q.^2).*t+N(x).*((1-q.^2).*(a+t)-k));
    P(x+1) = P(x).*(1-c-s.*(1-t)+N(x+1).*s.*(k-a-t))./(1-s+N(x+1).*k.*s+(1-q.^2).*(t.*s-c-N(x+1).*s.*(a+t)));
end

neq = (t.*s - c)./(t.*s+a.*s); 
peq = 1-sqrt(1-k./(a+t));

plot(neq,peq,'ko')
hold on
plot(N,P, 'k')
xlim([0 1]), ylim([0 1])