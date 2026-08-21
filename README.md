# SyndProxy private pool

## Current pool

- Alive now: 1086
- Gold now: 426
- HTTP: 365 alive / 107 gold
- HTTPS: 240 alive / 26 gold
- SOCKS4: 235 alive / 153 gold
- SOCKS5: 246 alive / 140 gold

## Historical pool

- Discovered: 160022
- Ever alive: 30549
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
