# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 385
- HTTP: 266 alive / 82 gold
- HTTPS: 141 alive / 18 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 220 alive / 138 gold

## Historical pool

- Discovered: 155801
- Ever alive: 29399
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
