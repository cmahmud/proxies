# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 379
- HTTP: 92 alive / 51 gold
- HTTPS: 56 alive / 12 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33495
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
