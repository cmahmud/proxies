# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 408
- HTTP: 347 alive / 92 gold
- HTTPS: 239 alive / 14 gold
- SOCKS4: 244 alive / 149 gold
- SOCKS5: 285 alive / 153 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21067
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
