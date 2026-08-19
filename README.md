# SyndProxy private pool

## Current pool

- Alive now: 1336
- Gold now: 390
- HTTP: 480 alive / 93 gold
- HTTPS: 315 alive / 17 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 321 alive / 151 gold

## Historical pool

- Discovered: 134541
- Ever alive: 22008
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
