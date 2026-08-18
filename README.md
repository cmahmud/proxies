# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 258
- HTTP: 311 alive / 30 gold
- HTTPS: 165 alive / 9 gold
- SOCKS4: 227 alive / 118 gold
- SOCKS5: 234 alive / 101 gold

## Historical pool

- Discovered: 94373
- Ever alive: 10175
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
