# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 466
- HTTP: 375 alive / 137 gold
- HTTPS: 241 alive / 91 gold
- SOCKS4: 212 alive / 128 gold
- SOCKS5: 208 alive / 110 gold

## Historical pool

- Discovered: 117111
- Ever alive: 17415
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
