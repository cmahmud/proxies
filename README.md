# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 415
- HTTP: 97 alive / 64 gold
- HTTPS: 74 alive / 21 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 37018
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
