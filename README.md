# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 299
- HTTP: 344 alive / 64 gold
- HTTPS: 227 alive / 19 gold
- SOCKS4: 201 alive / 113 gold
- SOCKS5: 210 alive / 103 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15510
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
