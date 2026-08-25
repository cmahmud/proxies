# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 417
- HTTP: 104 alive / 69 gold
- HTTPS: 85 alive / 18 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34823
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
