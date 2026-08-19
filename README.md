# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 498
- HTTP: 407 alive / 148 gold
- HTTPS: 279 alive / 90 gold
- SOCKS4: 219 alive / 123 gold
- SOCKS5: 251 alive / 137 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17282
- Ever gold: 661

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
