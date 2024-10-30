import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-description-example',
  templateUrl: './description-example.component.html',
  styleUrls: ['./description-example.component.css']
})
export class DescriptionExampleComponent {

  constructor(private router: Router) { }

  goBack(){
    this.router.navigate(['/solario1'])
  }
}
