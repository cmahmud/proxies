# SyndProxy private pool

## Current pool

- Alive now: 1323
- Gold now: 562
- HTTP: 507 alive / 188 gold
- HTTPS: 367 alive / 94 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 226 alive / 134 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22943
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
