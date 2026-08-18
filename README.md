# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 232
- HTTP: 186 alive / 28 gold
- HTTPS: 98 alive / 8 gold
- SOCKS4: 222 alive / 113 gold
- SOCKS5: 202 alive / 83 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7594
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
