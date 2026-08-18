# SyndProxy private pool

## Current pool

- Alive now: 670
- Gold now: 251
- HTTP: 178 alive / 31 gold
- HTTPS: 100 alive / 8 gold
- SOCKS4: 214 alive / 131 gold
- SOCKS5: 178 alive / 81 gold

## Historical pool

- Discovered: 94345
- Ever alive: 9683
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
