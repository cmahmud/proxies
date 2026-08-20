# SyndProxy private pool

## Current pool

- Alive now: 1472
- Gold now: 596
- HTTP: 493 alive / 196 gold
- HTTPS: 439 alive / 89 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 307 alive / 164 gold

## Historical pool

- Discovered: 140459
- Ever alive: 23609
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
