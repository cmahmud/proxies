# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 402
- HTTP: 233 alive / 87 gold
- HTTPS: 149 alive / 23 gold
- SOCKS4: 218 alive / 139 gold
- SOCKS5: 232 alive / 153 gold

## Historical pool

- Discovered: 151689
- Ever alive: 27789
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
