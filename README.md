# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 415
- HTTP: 338 alive / 99 gold
- HTTPS: 210 alive / 30 gold
- SOCKS4: 207 alive / 135 gold
- SOCKS5: 229 alive / 151 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31089
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
