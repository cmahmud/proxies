# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 598
- HTTP: 366 alive / 191 gold
- HTTPS: 311 alive / 101 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 235 alive / 160 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23458
- Ever gold: 921

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
