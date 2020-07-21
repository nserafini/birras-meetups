import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-toobar',
  templateUrl: './toobar.component.html',
  styleUrls: ['./toobar.component.css']
})
export class ToobarComponent implements OnInit {
  isLogged: boolean = false;
  isAdmin: boolean = false;
  
  constructor(private userService: UserService) { }

  ngOnInit(): void {    
    this.isLogged = this.userService.isLogged()
    if(this.isLogged){
      this.userService.getRoles(this.userService.getUserId()).subscribe(roles => {
        Object(roles).forEach((role) => {if(role["name"] == "admin"){this.isAdmin = true;}})
      })
    }
  }
}
