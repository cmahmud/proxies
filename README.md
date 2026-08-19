# SyndProxy private pool

## Current pool

- Alive now: 1279
- Gold now: 407
- HTTP: 468 alive / 106 gold
- HTTPS: 289 alive / 25 gold
- SOCKS4: 222 alive / 130 gold
- SOCKS5: 300 alive / 146 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22583
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
