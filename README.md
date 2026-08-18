# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 273
- HTTP: 290 alive / 35 gold
- HTTPS: 147 alive / 8 gold
- SOCKS4: 246 alive / 138 gold
- SOCKS5: 181 alive / 92 gold

## Historical pool

- Discovered: 102899
- Ever alive: 13879
- Ever gold: 431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
