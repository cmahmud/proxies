# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 425
- HTTP: 110 alive / 75 gold
- HTTPS: 91 alive / 22 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35007
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
