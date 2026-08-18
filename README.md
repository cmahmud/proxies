# SyndProxy private pool

## Current pool

- Alive now: 578
- Gold now: 226
- HTTP: 178 alive / 37 gold
- HTTPS: 88 alive / 10 gold
- SOCKS4: 156 alive / 102 gold
- SOCKS5: 156 alive / 77 gold

## Historical pool

- Discovered: 86651
- Ever alive: 5727
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
