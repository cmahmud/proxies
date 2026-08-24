# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 378
- HTTP: 89 alive / 50 gold
- HTTPS: 51 alive / 13 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 177 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33495
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
