clear all
close all

L0=2.5;
L1=0.5;
L2=2;
L3=1.2; 
L_PA=4;
alpha=20;


w2=1.5;
theta2=0:2:360;

for i=1:length(theta2)
    
    AC(i)=sqrt(L0^2+L1^2-2*L0*L1*cosd(theta2(i)));
    beta(i)=acosd((L0^2+AC(i)^2-L1^2)/(2*L0*AC(i)));
    psi(i)=acosd((L2^2+AC(i)^2-L3^2)/(2*L2*AC(i)));
    lamda(i)=acosd((L3^2+AC(i)^2-L2^2)/(2*L3*AC(i)));
    
    theta3(i)=psi(i)-beta(i);
    theta4(i)=180-lamda(i)-beta(i);
    
    if theta2(i)>180
        theta3(i)=psi(i)+beta(i);
        theta4(i)=180-lamda(i)+beta(i);
    end
    
    Ox(i)=0;
    Oy(i)=0;
    
    Ax(i)=Ox(i)+L1*cosd(theta2(i));
    Ay(i)=Oy(i)+L1*sind(theta2(i));
    
    Bx(i)=Ox(i)+Ax(i)+L2*cosd(theta3(i));
    By(i)=Ox(i)+Ay(i)+L2*sind(theta3(i));
    
    Cx(i)=L0;
    Cy(i)=0;
    
    Px(i)=Ax(i)+L_PA*cosd(alpha+theta3(i));
    Py(i)=Ay(i)+L_PA*sind(alpha+theta3(i));
    
    r=[L2*cosd(theta3(i)),-L3*cosd(theta4(i));L2*sind(theta3(i)),-L3*sind(theta4(i))];
    
    v=[-L1*w2*cosd(theta2(i));-L1*w2*sind(theta2(i))];
    
    w(i,:)=inv(r)*v;
    cm2(i)=w(i,1);
    cm4(i)=w(i,2);
    
    theta5(i)=alpha+theta3(i);
    
    V_Px(i)=-L1*sind(theta2(i))*w2-L_PA*sind(theta5(i))*cm2(i);
    V_Py(i)=L1*cosd(theta2(i))*w2+L_PA*cosd(theta5(i))*cm2(i);
    
    plot([Ox(i) Ax(i)],[Oy(i) Ay(i)],[Ax(i) Bx(i)],[Ay(i) By(i)], ...
         [Bx(i) Cx(i)],[By(i) Cy(i)],'LineWidth',3)
    hold on
    plot([Ax(i) Px(i)],[Ay(i) Py(i)],[Bx(i) Px(i)],[By(i) Py(i)],'LineWidth',3)
    
     grid on;
     axis equal;
     axis ([-5 15 -5 10]);
     drawnow;
     hold off;
     
     plot(Px,Py)
end

figure(2)
plot(theta2,V_Px,'LineWidth',3)
title('x-component of velocity of point P (*10cm/s)')
xlabel('angle of theta2')
ylabel('x-component of velocity of point P (*10cm/s)')


figure(3)
plot(theta2,V_Py,'LineWidth',3)
title('y-component of velocity of point P (*10cm/s)')
ylabel('y-component of velocity of point P (*10cm/s)')
xlabel('angle of theta2')