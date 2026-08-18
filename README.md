# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 319
- HTTP: 287 alive / 40 gold
- HTTPS: 167 alive / 9 gold
- SOCKS4: 236 alive / 138 gold
- SOCKS5: 223 alive / 132 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14271
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
