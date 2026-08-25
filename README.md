# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 413
- HTTP: 102 alive / 71 gold
- HTTPS: 76 alive / 14 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34857
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
