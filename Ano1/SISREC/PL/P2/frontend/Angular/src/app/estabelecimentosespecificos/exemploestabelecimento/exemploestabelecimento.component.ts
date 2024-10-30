import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PlacesService } from 'src/app/_services/places.service';

@Component({
  selector: 'app-exemploestabelecimento',
  templateUrl: './exemploestabelecimento.component.html',
  styleUrls: ['./exemploestabelecimento.component.css']
})
export class ExemploestabelecimentoComponent {
  name: string = '';
  address: string = '';
  image: string = '';

  constructor(private placesService: PlacesService, private router: Router) { }
  ngOnInit() {
    this.carregarSolario();
  }

  carregarSolario() {
    const nomeSolario = 'Solario 1';

    this.placesService.getPlace(nomeSolario).subscribe(
      (solario: any) => {
        this.name = solario.name;
        this.address = solario.address;
        this.image = solario.image;
      },
      error => {
        console.error('Erro ao buscar informações do solário:', error);
      }
    );
  }
  redirectAppointment(){
    this.router.navigate(['/appointment1']);
  }
  redirectDescription(){
    this.router.navigate(['/description1']);

  }
  goBack(){
    this.router.navigate(['/solarios'])
  }
}