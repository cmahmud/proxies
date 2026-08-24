# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 413
- HTTP: 127 alive / 74 gold
- HTTPS: 72 alive / 18 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 181471
- Ever alive: 33763
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
