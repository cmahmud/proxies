# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 416
- HTTP: 382 alive / 93 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 212 alive / 152 gold
- SOCKS5: 246 alive / 148 gold

## Historical pool

- Discovered: 158253
- Ever alive: 30081
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
