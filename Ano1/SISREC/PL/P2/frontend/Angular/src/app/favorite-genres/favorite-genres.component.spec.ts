import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FavoriteGenresComponent } from './favorite-genres.component';

describe('FavoriteGenresComponent', () => {
  let component: FavoriteGenresComponent;
  let fixture: ComponentFixture<FavoriteGenresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FavoriteGenresComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FavoriteGenresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
