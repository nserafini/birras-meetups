import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ToolbarAdminActionsComponent } from './toolbar-admin-actions.component';

describe('ToolbarAdminActionsComponent', () => {
  let component: ToolbarAdminActionsComponent;
  let fixture: ComponentFixture<ToolbarAdminActionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ToolbarAdminActionsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ToolbarAdminActionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
