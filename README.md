# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 374
- HTTP: 338 alive / 72 gold
- HTTPS: 210 alive / 20 gold
- SOCKS4: 202 alive / 120 gold
- SOCKS5: 244 alive / 162 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26108
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
