function delta_est = estimate(se_in, neighbors, N, sensor_est_history)
% FILE: estimate.m implemenets a consensus-based estimation protocol
%
% DESCRIPTION:
% Each agent updates their own estimate of a sensor value by applying the
% consensus protocol with its neighbors.
%
% INPUTS:
% se_in - everyone's original sensor estimates
%
% OUTPUTS:
% delta_est - the change in estimate required to arrive at a consensus with
% neighbors about the estimate
%
% TODO:
% Become resilient to estimates from unknown, bad faith actors

%% Authors: Safwan Alam, Musad Haque - 2019
%%%%%%%%%%%%%

delta_est = zeros(N, 1);
RR = 0;

for ii = 1:1:N
    for jj = 1:1:N
        if ((ii ~= jj) && neighbors(ii, jj))
            %Regular consensus with neighbors
            if size(sensor_est_history, 2) > 1
                for RR = 1:1:size(sensor_est_history, 2) % size of est history
                    if sensor_est_history(RR,1) == sensor_est_history(RR,end)
                        break
                    end
                end
            end
            %Susceptible to bad faith actors
            if (size(sensor_est_history, 2) == 1 || isempty(sensor_est_history) || RR ~= jj)     
                delta_est(ii, 1) = delta_est(ii, 1) - (se_in(ii, 1) - se_in(jj, 1));
            end
        end
    end
end
               
        
end


