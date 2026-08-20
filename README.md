# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 385
- HTTP: 172 alive / 76 gold
- HTTPS: 114 alive / 20 gold
- SOCKS4: 203 alive / 139 gold
- SOCKS5: 213 alive / 150 gold

## Historical pool

- Discovered: 145561
- Ever alive: 25509
- Ever gold: 1063

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
