function [p] = Kernel_F(Nx, Ny, lambda, z, delta_x)

p = zeros (Nx,Nx);

for ii = 1:Nx
    for jj = 1:Ny
        u = ii.*delta_x;
        v = jj.*delta_x;
        p(ii, jj) = exp((-1i*pi/(lambda*z))*(u.^2 + v.^2));
    end
end