# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 415
- HTTP: 120 alive / 69 gold
- HTTPS: 108 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35246
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
