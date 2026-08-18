# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 251
- HTTP: 216 alive / 23 gold
- HTTPS: 116 alive / 2 gold
- SOCKS4: 199 alive / 117 gold
- SOCKS5: 208 alive / 109 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11508
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
