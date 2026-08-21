# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 437
- HTTP: 405 alive / 108 gold
- HTTPS: 292 alive / 30 gold
- SOCKS4: 205 alive / 154 gold
- SOCKS5: 259 alive / 145 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28632
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
