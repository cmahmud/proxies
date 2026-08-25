# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 413
- HTTP: 113 alive / 70 gold
- HTTPS: 98 alive / 19 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34954
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
