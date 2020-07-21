import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { MeetupService } from '../../services/meetup.service';
import { FormBuilder, FormGroup, FormArray, FormControl, ValidatorFn } from '@angular/forms';
import { of } from 'rxjs';

@Component({
  selector: 'app-meetup-create',
  templateUrl: './meetup-create.component.html',
  styleUrls: ['./meetup-create.component.css']
})
export class MeetupCreateComponent implements OnInit {
  form: FormGroup;
  users;


  constructor(
    private userService: UserService, 
    private meetupService: MeetupService,
    private formBuilder: FormBuilder
  ) {
    this.form = this.formBuilder.group({
      name: new FormControl(),
      description: new FormControl(),
      date: new FormControl(),
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

    let data = {
      'name': this.form.value.name,
      'description': this.form.value.description,
      'date': this.form.value.date,
      'users': selectedUserIds
    }
    this.meetupService.create(data).subscribe(response => {console.log(response)});
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
