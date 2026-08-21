# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 398
- HTTP: 234 alive / 84 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 213 alive / 139 gold
- SOCKS5: 238 alive / 151 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27792
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
