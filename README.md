# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 418
- HTTP: 124 alive / 71 gold
- HTTPS: 96 alive / 22 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35294
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
