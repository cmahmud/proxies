# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 415
- HTTP: 92 alive / 66 gold
- HTTPS: 60 alive / 23 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47032
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
