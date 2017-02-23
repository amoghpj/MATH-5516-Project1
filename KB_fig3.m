function FREQ=KB_fig3(q,n,k,a,s,t,c,m,tmax)
    N(1) = n;
    Q(1) = q;
    FREQ=[];
    PRECISION=1e4;
    for x = 1:tmax
        q=Q(x);
        p=1-q;
        P(x)=1-Q(x);
        N(x+1) = (N(x).*(1-k+(1-q.^2).*a))./(1-(1-q.^2).*t+N(x).*((1-q.^2).*(a+t)-k));
        P(x+1) = P(x).*(1-c-s.*(1-t)+N(x+1).*s.*(k-a-t))./(1-s+N(x+1).*k.*s+(1-q.^2).*(t.*s-c-N(x+1).*s.*(a+t)));
        Q(x+1) = 1-P(x+1); 
        N(x+1) = (N(x+1)+m.*(1-2.*N(x+1))).*(1+(rand).*(1./1e4)-(0.5./1e4));
        Q(x+1) = (Q(x+1)+m.*(1-2.*Q(x+1))).*(1+(rand).*(1./(2.*1e4))-(0.5./(2.*1e4)));
        N(x+1) = round(N(x+1).*PRECISION)./PRECISION;
        Q(x+1) = round(Q(x+1).*PRECISION)./PRECISION;
    end
    FREQ(1,:)=Q;
    FREQ(2,:)=N;
end