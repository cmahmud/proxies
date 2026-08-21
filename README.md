# SyndProxy private pool

## Current pool

- Alive now: 798
- Gold now: 413
- HTTP: 254 alive / 91 gold
- HTTPS: 126 alive / 23 gold
- SOCKS4: 205 alive / 146 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27833
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
