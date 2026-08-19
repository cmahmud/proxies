# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 468
- HTTP: 322 alive / 135 gold
- HTTPS: 249 alive / 90 gold
- SOCKS4: 204 alive / 130 gold
- SOCKS5: 192 alive / 113 gold

## Historical pool

- Discovered: 117111
- Ever alive: 17357
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
