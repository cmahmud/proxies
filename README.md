# SyndProxy private pool

## Current pool

- Alive now: 966
- Gold now: 243
- HTTP: 430 alive / 33 gold
- HTTPS: 149 alive / 6 gold
- SOCKS4: 231 alive / 139 gold
- SOCKS5: 156 alive / 65 gold

## Historical pool

- Discovered: 102867
- Ever alive: 13645
- Ever gold: 426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
