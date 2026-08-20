# SyndProxy private pool

## Current pool

- Alive now: 1389
- Gold now: 582
- HTTP: 485 alive / 190 gold
- HTTPS: 346 alive / 102 gold
- SOCKS4: 235 alive / 134 gold
- SOCKS5: 323 alive / 156 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23217
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
