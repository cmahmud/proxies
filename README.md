# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 338
- HTTP: 284 alive / 82 gold
- HTTPS: 211 alive / 26 gold
- SOCKS4: 206 alive / 140 gold
- SOCKS5: 180 alive / 90 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32502
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
