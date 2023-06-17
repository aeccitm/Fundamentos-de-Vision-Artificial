clear all
clc

lambda = 532e-9; % longitud de onda en metros

delta_x = 4.5e-6;
delta_y = delta_x;
z = 0.9; % distancia

hologramOI = (imread('H2.tif')); 
hologramO = im2uint16(hologramOI);
[Nx, Ny] = size(hologramO);

reconstructionO = zeros(Nx,Ny);
original = ifft2(fft2(hologramO));

trans = ifft2(hologramO);
imag_trans = imag(trans);
real_trans = real(trans);

mag_trans = abs(trans);

%figure, imagesc(mag_trans);

[J,rect] = imcrop(mag_trans);

rec_trans = imcrop(original,rect);

tam = size(rec_trans);
i = round((Nx-tam(1))/2);
j = round((Ny-tam(2))/2);

B = padarray(rec_trans,[i j],0,'both');
HI = imresize(B,[Nx Ny]);

prop = Kernel_F(Nx, Ny, lambda, z, delta_x);

%figure, imshow(abs(trans));
%figure, imagesc(HI);
%figure, imshow(real_trans);

%U = ifft2(original.*prop);
U = ifft2(HI.*prop);
recO = abs(U);

reconstructionO(:,:) = recO(:,:);
% showing reconstructed object transmission function

figure;
imshow(reconstructionO(:,:));