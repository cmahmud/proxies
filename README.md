# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 417
- HTTP: 120 alive / 68 gold
- HTTPS: 109 alive / 22 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35306
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
