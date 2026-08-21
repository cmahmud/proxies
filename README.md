# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 402
- HTTP: 355 alive / 109 gold
- HTTPS: 263 alive / 23 gold
- SOCKS4: 217 alive / 148 gold
- SOCKS5: 221 alive / 122 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28536
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
