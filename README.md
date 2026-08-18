# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 297
- HTTP: 321 alive / 34 gold
- HTTPS: 182 alive / 5 gold
- SOCKS4: 219 alive / 132 gold
- SOCKS5: 219 alive / 126 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13260
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
