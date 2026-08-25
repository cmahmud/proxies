# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 415
- HTTP: 96 alive / 62 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35597
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
