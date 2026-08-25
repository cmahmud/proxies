# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 413
- HTTP: 102 alive / 67 gold
- HTTPS: 76 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35366
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
