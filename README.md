# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 436
- HTTP: 145 alive / 84 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 186 alive / 159 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34748
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
