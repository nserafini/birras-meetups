import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import {MatSnackBar} from '@angular/material/snack-bar';
import {Router} from "@angular/router"


@Component({
  template: ''
})
export class LogoutComponent implements OnInit {

  constructor(
    private userService: UserService,
    private router: Router,
    private _snackBar: MatSnackBar
  ) { }

  ngOnInit(): void {
    this.userService.logout().subscribe(response => {
      this.router.navigate(['/login']);        
      this._snackBar.open("Cerraste sesión", "Cerrar", {
        duration: 5000,
        horizontalPosition: "center",
        verticalPosition: "top",
      });
    })
  }

}
