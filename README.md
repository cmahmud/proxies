# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 413
- HTTP: 105 alive / 74 gold
- HTTPS: 69 alive / 17 gold
- SOCKS4: 162 alive / 157 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33731
- Ever gold: 1249

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
