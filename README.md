# SyndProxy private pool

## Current pool

- Alive now: 1199
- Gold now: 537
- HTTP: 437 alive / 187 gold
- HTTPS: 327 alive / 78 gold
- SOCKS4: 223 alive / 131 gold
- SOCKS5: 212 alive / 141 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19794
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
