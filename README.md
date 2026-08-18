# SyndProxy private pool

## Current pool

- Alive now: 577
- Gold now: 227
- HTTP: 144 alive / 27 gold
- HTTPS: 74 alive / 7 gold
- SOCKS4: 158 alive / 111 gold
- SOCKS5: 201 alive / 82 gold

## Historical pool

- Discovered: 91695
- Ever alive: 8361
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
