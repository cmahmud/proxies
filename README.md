# SyndProxy private pool

## Current pool

- Alive now: 1676
- Gold now: 651
- HTTP: 595 alive / 214 gold
- HTTPS: 487 alive / 116 gold
- SOCKS4: 249 alive / 160 gold
- SOCKS5: 345 alive / 161 gold

## Historical pool

- Discovered: 141249
- Ever alive: 24152
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
