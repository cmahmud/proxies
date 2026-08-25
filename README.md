# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 419
- HTTP: 110 alive / 71 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35060
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
