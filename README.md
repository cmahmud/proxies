# SyndProxy private pool

## Current pool

- Alive now: 1249
- Gold now: 404
- HTTP: 407 alive / 93 gold
- HTTPS: 310 alive / 19 gold
- SOCKS4: 234 alive / 139 gold
- SOCKS5: 298 alive / 153 gold

## Historical pool

- Discovered: 135761
- Ever alive: 22204
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
