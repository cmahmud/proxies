# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 415
- HTTP: 93 alive / 67 gold
- HTTPS: 77 alive / 22 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 171 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37056
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
