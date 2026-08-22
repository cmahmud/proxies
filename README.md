# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 397
- HTTP: 257 alive / 90 gold
- HTTPS: 187 alive / 30 gold
- SOCKS4: 202 alive / 141 gold
- SOCKS5: 209 alive / 136 gold

## Historical pool

- Discovered: 162762
- Ever alive: 31611
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
