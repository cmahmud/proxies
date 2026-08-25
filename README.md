# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 415
- HTTP: 123 alive / 65 gold
- HTTPS: 81 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35407
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
