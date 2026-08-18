# SyndProxy private pool

## Current pool

- Alive now: 689
- Gold now: 252
- HTTP: 169 alive / 29 gold
- HTTPS: 124 alive / 8 gold
- SOCKS4: 183 alive / 112 gold
- SOCKS5: 213 alive / 103 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10225
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
