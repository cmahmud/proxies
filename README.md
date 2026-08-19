# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 354
- HTTP: 336 alive / 71 gold
- HTTPS: 204 alive / 16 gold
- SOCKS4: 231 alive / 146 gold
- SOCKS5: 208 alive / 121 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16049
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
