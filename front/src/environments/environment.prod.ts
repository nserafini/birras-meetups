import { HttpHeaders } from '@angular/common/http';

export const environment = {
  production: true,
  API_URL: 'http://'+window.location.hostname+':5000',
  API_HEADERS: {
    headers: new HttpHeaders ({
      'X-API-Key': 'secret',
    }),
    withCredentials: true
  }
};
