# SyndProxy private pool

## Current pool

- Alive now: 1265
- Gold now: 417
- HTTP: 421 alive / 98 gold
- HTTPS: 281 alive / 18 gold
- SOCKS4: 252 alive / 142 gold
- SOCKS5: 311 alive / 159 gold

## Historical pool

- Discovered: 131825
- Ever alive: 20970
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
