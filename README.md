# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 397
- HTTP: 313 alive / 81 gold
- HTTPS: 199 alive / 22 gold
- SOCKS4: 208 alive / 145 gold
- SOCKS5: 253 alive / 149 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29981
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
