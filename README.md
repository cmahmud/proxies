# SyndProxy private pool

## Current pool

- Alive now: 763
- Gold now: 413
- HTTP: 203 alive / 90 gold
- HTTPS: 135 alive / 24 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 213 alive / 160 gold

## Historical pool

- Discovered: 151687
- Ever alive: 27724
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
