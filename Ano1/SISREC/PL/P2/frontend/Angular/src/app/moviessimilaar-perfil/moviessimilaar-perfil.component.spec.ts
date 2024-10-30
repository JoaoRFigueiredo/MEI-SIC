import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MoviessimilaarPerfilComponent } from './moviessimilaar-perfil.component';

describe('MoviessimilaarPerfilComponent', () => {
  let component: MoviessimilaarPerfilComponent;
  let fixture: ComponentFixture<MoviessimilaarPerfilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MoviessimilaarPerfilComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MoviessimilaarPerfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
