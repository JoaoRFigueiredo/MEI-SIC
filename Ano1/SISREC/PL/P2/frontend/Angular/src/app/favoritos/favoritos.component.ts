import { Component } from '@angular/core';
import { AuthService } from '../_services/auth.service';
import { Router } from '@angular/router';
import { PlacesService } from '../_services/places.service';

@Component({
  selector: 'app-favoritos',
  templateUrl: './favoritos.component.html',
  styleUrls: ['./favoritos.component.css']
})
export class FavoritosComponent {
  userEmail: string= '';
  favoritos: any[] = [];

  constructor(private authService: AuthService,private router: Router,private placesService: PlacesService) {}
  
  ngOnInit() {
    this.carregarSolarios();
  }
  carregarSolarios() {
    this.authService.getFavorites(this.authService.getUserEmail()).subscribe(
      (data: any) => {
        this.favoritos = [];
  
        // Iterar sobre os nomes dos lugares favoritos
        for (const nomePlace of data) {
          // Chamar o método getPlace para obter o Place correspondente ao nome
          this.placesService.getPlace(nomePlace).subscribe(
            (place: any) => {
              // Adicionar o Place à lista de favoritos
              this.favoritos.push(place);
            },
            error => {
              console.error(`Erro ao buscar o lugar ${nomePlace}:`, error);
            }
          );
        }
      },
      error => {
        console.error('Erro ao buscar solários:', error);
      }
    );
  }
  
  redirect(nomesolario:string){
    console.log("o nome do solario é ->" + nomesolario)
    const nomesolarioendpoint = nomesolario.replace(/\s/g, '').toLowerCase();
    console.log("o nome do solario depois de tratado é ->" + nomesolarioendpoint)
    const newurl = '/' + nomesolarioendpoint;
    this.router.navigate([newurl]);
  }

  goBack(){
    this.router.navigate(['/board-client'])
  }
}
