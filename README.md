# SyndProxy private pool

## Current pool

- Alive now: 936
- Gold now: 336
- HTTP: 303 alive / 80 gold
- HTTPS: 244 alive / 26 gold
- SOCKS4: 198 alive / 140 gold
- SOCKS5: 191 alive / 90 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32499
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
