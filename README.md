# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 413
- HTTP: 99 alive / 63 gold
- HTTPS: 84 alive / 22 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35478
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
