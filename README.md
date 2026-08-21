# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 391
- HTTP: 246 alive / 88 gold
- HTTPS: 113 alive / 25 gold
- SOCKS4: 190 alive / 121 gold
- SOCKS5: 232 alive / 157 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29468
- Ever gold: 1128

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
