# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 420
- HTTP: 125 alive / 71 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35301
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
