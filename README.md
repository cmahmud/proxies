# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 458
- HTTP: 384 alive / 125 gold
- HTTPS: 267 alive / 77 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 182 alive / 114 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17463
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
