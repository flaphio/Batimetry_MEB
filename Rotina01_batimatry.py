#################################################################################################
'Análise das trajetórias de derivadores na Plataforma Continental Amazônica'
'Autores: Francisco Flávio Borges, Pedro Paulo de Freitas '

# Carregando pacotes
import numpy as np
import cmocean
import datetime
import geopy.distance
import scipy.io as io
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
from matplotlib.ticker import FormatStrFormatter
from mpl_toolkits.axes_grid1 import make_axes_locatable
##################################################################################################
path = r'C:/Users/engfl/OneDrive/Documentos/Derivadores_PCAmazonia/Passo01 _Batimetria_Gradiente/batimetria/' 
path_fig = r'C:/Users/engfl/OneDrive/Documentos/Derivadores_PCAmazonia/Passo01 _Batimetria_Gradiente/figuras/' 
##################################################################################################
d = io.loadmat(path+'batimetria.mat')
lon=d['lon']
lat=d['lat']
bat=d['bat']*(-1)
#
plt.ion()
plt.close('all')
fig, ax = plt.subplots(1,figsize=(22, 12))
pos1 = ax.get_position()
pos2 = [pos1.x0 , pos1.y0,  pos1.width, pos1.height] 
hh1=ax.set_position(pos2) # set a new position
llcrnrlon=-55
urcrnrlon=-30
llcrnrlat=-6
urcrnrlat=6
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
           urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,
           projection='merc', resolution='l')
# limits=(0,20,40,60,80,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1200,1400,1600,1800,2000,3000)
limits=[-2000,-1000,-500,-200,-100,-50,-10]
cores=24
hh1=m.contourf(lon, lat,bat,limits,cmap='bone_r',extend='both',latlon=True)
# cc1=m.contour(lon,lat,bat,[-10],colors='r',linestyles = 'solid',latlon=True)
cc2=m.contour(lon,lat,bat,[-50],colors='red',linestyles = 'solid',latlon=True)
cc3=m.contour(lon,lat,bat,[-100],colors='b',linestyles = 'solid',latlon=True)
# cc4=m.contour(lon,lat,bat,[-200],colors='m',linestyles = 'solid',latlon=True)


#Nomeando setores dos estados 
px1,py1=m(-37,-6.1)
plt.text(px1,py1,u'RN',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
cx1,cy1=m(-39.5,-5)
plt.text(cx1,cy1,u'CE',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
bx1,by1=m(-42.5,-5)
plt.text(bx1,by1,u'PI',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
pmx1,pmy1=m(-45.5,-5)
plt.text(pmx1,pmy1,u'MA',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
fx1,fy1=m(-52.5,-5)
plt.text(fx1,fy1,u'PA',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
fx1,fy1=m(-52.5,2)
plt.text(fx1,fy1,u'AP',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
################################################################################################


# hh1=m.contourf(lon, lat,bat,limits,cmap=cmocean.cm.deep,extend='both',latlon=True)
llcrnrlon=llcrnrlon
urcrnrlon=urcrnrlon
llcrnrlat=llcrnrlat
urcrnrlat=urcrnrlat
m.drawstates()
m.drawcoastlines()

m.fillcontinents(color='0.85')
meridians = np.arange(llcrnrlon, urcrnrlon + 1, 5)
parallels = np.arange(llcrnrlat, urcrnrlat + 1, 2)
m.drawparallels(parallels, linewidth=1, labels=[1, 0, 0, 0],fontsize=20,fontweight='bold')
m.drawmeridians(meridians, linewidth=1, labels=[0, 0, 0, 1],fontsize=20,fontweight='bold')
m.llcrnrlon = llcrnrlon
m.urcrnrlon = urcrnrlon
m.llcrnrlat = llcrnrlat
m.urcrnrlat = urcrnrlat
m.ax = ax 
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.05)
cb = plt.colorbar(hh1,cax=cax)
cb.ax.set_title(u"[m]",fontsize=16,fontweight='bold', y=1.02)#setando texto do
cb.ax.tick_params(labelsize=20)
plt.savefig(path_fig+'Mapa_batimetria_PCA.png', bbox_inches='tight')
plt.close()

#### Análise a batimetria da Plataforma Continenal Amazônica (PCA) : cálculo do gradiente batimétrico;
#### definição de uma fronteira da PCA e definição de setores da PCA.

import richdem as rd
import numpy as np

rda = rd.rdarray(bat.T*(-1), no_data=-9999)
slope = rd.TerrainAttribute(rda, attrib='slope_riserun')
# slope = rd.TerrainAttribute(rda, attrib='slope_degrees')
aspect = rd.TerrainAttribute(rda, attrib='aspect')

##################################################################################################
##################################################################################################
path = r'C:/Users/engfl/OneDrive/Documentos/Derivadores_PCAmazonia/Passo01 _Batimetria_Gradiente/batimetria/' 
path_fig = r'C:/Users/engfl/OneDrive/Documentos/Derivadores_PCAmazonia/Passo01 _Batimetria_Gradiente/figuras/'
##################################################################################################
d = io.loadmat(path+'batimetria.mat')
lon=d['lon']
lat=d['lat']
bat=d['bat']*(-1)
##################################################################################################
'Mapa do BATHYMETRIC SLOPE'
plt.ion()
plt.close('all')
fig, ax = plt.subplots(1,figsize=(22, 12))
pos1 = ax.get_position()
pos2 = [pos1.x0 , pos1.y0,  pos1.width, pos1.height]
hh1=ax.set_position(pos2) # set a new position
llcrnrlon=-55
urcrnrlon=-30
llcrnrlat=-6
urcrnrlat=6
m = Basemap(llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,
           urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,
           projection='merc', resolution='l')
cores=100
limits=np.arange(0,41,1)
limits2=np.arange(0,50,10)
cores=100
hh1=m.contourf(lon,lat,slope.T,limits,cmap=plt.cm.get_cmap('bone_r', cores),extend='both',latlon=True)
cc3=m.contour(lon,lat,bat,[-100],colors='b',linewidth=15,linestyles = 'solid',latlon=True)
cc3=m.contour(lon,lat,bat,[-50],colors='r',linewidth=15,linestyles = 'solid',latlon=True)


#Definindo setores

"Bacia Potiguar"
# Seção inicial - Isobata: 2000 m 
mx1a,my1a=m(-35.0,-5.0)
mx2a,my2a=m(-31.0,-0.7)
m.plot([mx1a,mx2a],[my1a,my2a],color='m',linewidth=3)#pontos mmap da divisão da PCA - MA    
# Seção Final de Potiguar
mx1b,my1b=m(-38.45,-3.9)
mx2b,my2b=m(-37.2,1.0)
m.plot([mx1b,mx2b],[my1b,my2b],color='m',linewidth=3)#pontos mmap da divisão da PCA - MA    

"Bacia do Ceará"
# Delimitada entre o final da bacia potiguar e 
# o inicio da bacia de barreirinhas

"Bacia de Barreirinhas"
# Seção Inicial da bacia de barreirinhas
ax1a,ay1a=m(-41.8,-2.7)
ax2a,ay2a=m(-41,2.0)
m.plot([ax1a,ax2a],[ay1a,ay2a],color='m',linewidth=3)#pontos mmap da divisão da PCA - AP    
# Seção Final da baica de barreirinhas 
ax1b,ay1b=m(-44.6,-2.5)
ax2b,ay2b=m(-43.3,2.5)
m.plot([ax1b,ax2b],[ay1b,ay2b],color='m',linewidth=3)#pontos mmap da divisão da PCA - AP

"Bacia Pará-Maranhão"
# Delimitada entre o final da bacia de barreirinhas e 
# o inicio da bacia do Foz do Amazonas

"Bacia do foz do Amazonas"
# Seção Inicial da bacia do foz do Amazonas
ax1a,ay1a=m(-48,-0.9)
ax2a,ay2a=m(-45.5,3.0)
m.plot([ax1a,ax2a],[ay1a,ay2a],color='m',linewidth=3)#pontos mmap da divisão da PCA - AP    

# Seção Final da baica do foz do Amazonas
ax1b,ay1b=m(-51.6,4.0)
ax2b,ay2b=m(-49.5,6.0)
m.plot([ax1b,ax2b],[ay1b,ay2b],color='m',linewidth=3)#pontos mmap da divisão da PCA - AP

#Nomeando setores das bacias
px1,py1=m(-38.2,-5.9)
plt.text(px1,py1,u'B. Potiguar shelf',color='red',fontsize=12,fontweight='bold',style='italic',rotation=-35)
cx1,cy1=m(-41.0,-4.5)
plt.text(cx1,cy1,u'B. Ceará shelf',color='red',fontsize=12,fontweight='bold',style='italic',rotation=-35)
bx1,by1=m(-44.3,-4.5)
plt.text(bx1,by1,u'B. barreirinhas shelf',color='red',fontsize=9,fontweight='bold',style='italic',rotation=-35)
pmx1,pmy1=m(-48.0,-3.0)
plt.text(pmx1,pmy1,u'B. Pará-Maranhão shelf',color='red',fontsize=10,fontweight='bold',style='italic',rotation=-35)
fx1,fy1=m(-51,0.2)
plt.text(fx1,fy1,u'B. Foz_amazonas shelf',color='red',fontsize=13,fontweight='bold',style='italic',rotation= -50)
################################################################################################


#Nomeando setores dos estados 
px1,py1=m(-37,-6.1)
plt.text(px1,py1,u'RN',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
cx1,cy1=m(-39.5,-5)
plt.text(cx1,cy1,u'CE',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
bx1,by1=m(-42.5,-5)
plt.text(bx1,by1,u'PI',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
pmx1,pmy1=m(-45.5,-5)
plt.text(pmx1,pmy1,u'MA',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
fx1,fy1=m(-52.5,-5)
plt.text(fx1,fy1,u'PA',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
fx1,fy1=m(-52.5,2)
plt.text(fx1,fy1,u'AP',color='red',fontsize=15,fontweight='bold',style='italic',rotation=0)
################################################################################################

lcrnrlon=llcrnrlon
urcrnrlon=urcrnrlon
llcrnrlat=llcrnrlat
urcrnrlat=urcrnrlat
m.drawstates()
m.drawcoastlines()
m.fillcontinents(color='0.85')
meridians = np.arange(llcrnrlon, urcrnrlon + 1, 5)
parallels = np.arange(llcrnrlat, urcrnrlat + 1, 2)
m.drawparallels(parallels, linewidth=1, labels=[1, 0, 0, 0],fontsize=20,fontweight='bold')
m.drawmeridians(meridians, linewidth=1, labels=[0, 0, 0, 1],fontsize=20,fontweight='bold')
m.llcrnrlon = llcrnrlon
m.urcrnrlon = urcrnrlon
m.llcrnrlat = llcrnrlat
m.urcrnrlat = urcrnrlat
m.ax = ax
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="2%", pad=0.05)
cb = plt.colorbar(hh1,cax=cax,ticks=limits2)
cb.ax.set_yticklabels(['Low','','','','High'],fontsize=18)  # horizontal colorbar
cb.set_label('[Bathymetric Slope] ',labelpad=-10, y=0.5, rotation=-90,fontsize=16)
cb.ax.tick_params(labelsize=20)
plt.savefig(path_fig+'Gradiente_PCA.png', bbox_inches='tight')
# plt.close()