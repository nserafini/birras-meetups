import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { FormBuilder, FormGroup, FormControl, Validators } from '@angular/forms';
import {MatSnackBar} from '@angular/material/snack-bar';
import {Router} from "@angular/router"


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(
    private userService: UserService, 
    private formBuilder: FormBuilder,
    private router: Router,
    private _snackBar: MatSnackBar
  ) {
    this.form = this.formBuilder.group({
      user: new FormControl(null, Validators.required),
      password: new FormControl(null, Validators.required)
    });
  }

  submit() {
    if (this.form.invalid) {
      return;
    }

    let data = {
      'user': this.form.value.user,
      'password': this.form.value.password
    }

    this.userService.login(data).subscribe(response => {
        console.log(response)
        this.router.navigate(['/']);
        this._snackBar.open("Logueado con exito!", "Cerrar", {
          duration: 5000,
          horizontalPosition: "center",
          verticalPosition: "top",
        });
      },
      (err) => {
        this._snackBar.open("Ocurrió un error: verifica credenciales", "Cerrar", {
          duration: 5000,
          horizontalPosition: "center",
          verticalPosition: "top",
        });
        console.log(err)
    });
  }

  ngOnInit(): void {}
}
