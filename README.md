# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 413
- HTTP: 124 alive / 71 gold
- HTTPS: 63 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33744
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
