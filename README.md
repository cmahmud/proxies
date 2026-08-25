# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 415
- HTTP: 92 alive / 61 gold
- HTTPS: 70 alive / 21 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36233
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
