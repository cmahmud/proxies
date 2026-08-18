# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 263
- HTTP: 256 alive / 33 gold
- HTTPS: 177 alive / 5 gold
- SOCKS4: 210 alive / 120 gold
- SOCKS5: 246 alive / 105 gold

## Historical pool

- Discovered: 96706
- Ever alive: 11096
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
