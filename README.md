# SyndProxy private pool

## Current pool

- Alive now: 904
- Gold now: 407
- HTTP: 270 alive / 87 gold
- HTTPS: 176 alive / 23 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 251 alive / 164 gold

## Historical pool

- Discovered: 166560
- Ever alive: 32404
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
