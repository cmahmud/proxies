# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 401
- HTTP: 331 alive / 90 gold
- HTTPS: 258 alive / 24 gold
- SOCKS4: 195 alive / 134 gold
- SOCKS5: 221 alive / 153 gold

## Historical pool

- Discovered: 144729
- Ever alive: 24919
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
