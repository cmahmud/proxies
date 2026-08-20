# SyndProxy private pool

## Current pool

- Alive now: 1809
- Gold now: 655
- HTTP: 764 alive / 239 gold
- HTTPS: 588 alive / 141 gold
- SOCKS4: 213 alive / 134 gold
- SOCKS5: 244 alive / 141 gold

## Historical pool

- Discovered: 142719
- Ever alive: 24519
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
