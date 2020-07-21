import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { MeetupService } from '../../services/meetup.service';
import { FormBuilder, FormGroup, FormArray, FormControl, Validators, ValidatorFn } from '@angular/forms';
import {MatSnackBar} from '@angular/material/snack-bar';
import {Router} from "@angular/router"



@Component({
  selector: 'app-meetup-create',
  templateUrl: './meetup-create.component.html',
  styleUrls: ['./meetup-create.component.css']
})
export class MeetupCreateComponent implements OnInit {
  form: FormGroup;
  users;


  constructor(
    private meetupService: MeetupService,
    private userService: UserService, 
    private formBuilder: FormBuilder,
    private router: Router,
    private _snackBar: MatSnackBar
  ) {

    this.form = this.formBuilder.group({
      name: new FormControl(null, Validators.required),
      description: new FormControl(null, Validators.required),
      date: new FormControl(null, Validators.required),
      users: new FormArray([], minSelectedCheckboxes(1))
    });
    this.userService.getAll().subscribe(users => {
      this.users = users
      this.users.forEach(() => this.usersFormArray.push(new FormControl(false)));
    });
  }

  get usersFormArray() {
    return this.form.controls.users as FormArray;
  }

  submit() {
    const selectedUserIds = this.form.value.users
      .map((checked, i) => checked ? this.users[i].id : null)
      .filter(v => v !== null);

      if (this.form.invalid) {
        return;
      }

    let data = {
      'name': this.form.value.name,
      'description': this.form.value.description,
      'date': this.form.value.date,
      'users': selectedUserIds
    }

    this.meetupService.create(data).subscribe(response => {
      console.log(response)
      this.router.navigate([''])
      this._snackBar.open("Meet creada con éxito!", "Cerrar", {
        duration: 10000,
        horizontalPosition: "end",
        verticalPosition: "top",
      });
    },
    (err) => {
      this._snackBar.open("Ocurrio un error", "Cerrar", {
        duration: 10000,
        horizontalPosition: "end",
        verticalPosition: "top",
      });
      console.log(err)
    });
  }

  ngOnInit(): void {}
}

function minSelectedCheckboxes(min = 1) {
  const validator: ValidatorFn = (formArray: FormArray) => {
    const totalSelected = formArray.controls
      .map(control => control.value)
      .reduce((prev, next) => next ? prev + next : prev, 0);

    return totalSelected >= min ? null : { required: true };
  };

  return validator;
}
