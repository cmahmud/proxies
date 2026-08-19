# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 439
- HTTP: 302 alive / 121 gold
- HTTPS: 222 alive / 46 gold
- SOCKS4: 231 alive / 138 gold
- SOCKS5: 244 alive / 134 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16782
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
