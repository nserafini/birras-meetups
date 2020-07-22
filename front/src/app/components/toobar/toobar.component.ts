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
    this.userService.isLogged().then(logged => {
      this.isLogged = logged
      if(logged){
        this.userService.isAdmin().then(admin => {
          this.isAdmin = admin
        })
      }
    })
  }
}
