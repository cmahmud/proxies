# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 395
- HTTP: 305 alive / 93 gold
- HTTPS: 250 alive / 29 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 240 alive / 126 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31014
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
