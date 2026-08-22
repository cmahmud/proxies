# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 431
- HTTP: 330 alive / 95 gold
- HTTPS: 227 alive / 28 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 269 alive / 160 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31016
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
