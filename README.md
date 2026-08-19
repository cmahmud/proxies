# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 325
- HTTP: 272 alive / 65 gold
- HTTPS: 227 alive / 19 gold
- SOCKS4: 225 alive / 127 gold
- SOCKS5: 210 alive / 114 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15391
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
