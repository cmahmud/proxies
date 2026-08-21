# SyndProxy private pool

## Current pool

- Alive now: 1054
- Gold now: 405
- HTTP: 362 alive / 109 gold
- HTTPS: 249 alive / 25 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 220 alive / 123 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28537
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
