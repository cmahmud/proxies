# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 539
- HTTP: 356 alive / 151 gold
- HTTPS: 258 alive / 103 gold
- SOCKS4: 210 alive / 150 gold
- SOCKS5: 213 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19902
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
