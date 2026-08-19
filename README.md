# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 477
- HTTP: 348 alive / 123 gold
- HTTPS: 219 alive / 70 gold
- SOCKS4: 223 alive / 138 gold
- SOCKS5: 257 alive / 146 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16875
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
