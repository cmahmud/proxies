# SyndProxy private pool

## Current pool

- Alive now: 1385
- Gold now: 384
- HTTP: 504 alive / 82 gold
- HTTPS: 343 alive / 13 gold
- SOCKS4: 237 alive / 148 gold
- SOCKS5: 301 alive / 141 gold

## Historical pool

- Discovered: 134448
- Ever alive: 21792
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
