# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 417
- HTTP: 116 alive / 71 gold
- HTTPS: 112 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35251
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
