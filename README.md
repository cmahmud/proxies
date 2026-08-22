# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 412
- HTTP: 213 alive / 86 gold
- HTTPS: 168 alive / 29 gold
- SOCKS4: 202 alive / 138 gold
- SOCKS5: 249 alive / 159 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31417
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
