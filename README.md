# SyndProxy private pool

## Current pool

- Alive now: 866
- Gold now: 254
- HTTP: 356 alive / 32 gold
- HTTPS: 95 alive / 4 gold
- SOCKS4: 209 alive / 116 gold
- SOCKS5: 206 alive / 102 gold

## Historical pool

- Discovered: 95404
- Ever alive: 10834
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
