import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { AuthService } from 'src/app/_services/auth.service';
import { User } from 'src/app/_models/User';

@Component({
  selector: 'app-get-users',
  templateUrl: './get-users.component.html',
  styleUrls: ['./get-users.component.css']
})
export class GetUsersComponent implements OnInit {
  users: User[] = [];
  content ?: string;
  constructor(private authService: AuthService,
    private location: Location) { }

  ngOnInit(): void {
    this.DisplayAll();
  }

  goBack(): void {
    this.location.back();
  }

  DisplayAll(){
    this.users=[];
    this.authService.getUsers().subscribe(data => {
      this.users = data;
    },
    err => {
      this.content = JSON.parse(err.error).message;
      }
    )
  }
  deactivate(email:string){
    this.authService.inactive(email).subscribe(data => {
      this.DisplayAll();
    },
    err => {
      this.content = JSON.parse(err.error).message;
      }
    )
  }
}
