# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 413
- HTTP: 108 alive / 72 gold
- HTTPS: 92 alive / 13 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34872
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
