# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 413
- HTTP: 126 alive / 74 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 185 alive / 162 gold

## Historical pool

- Discovered: 181471
- Ever alive: 33764
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
