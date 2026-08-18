# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 251
- HTTP: 214 alive / 35 gold
- HTTPS: 142 alive / 8 gold
- SOCKS4: 213 alive / 125 gold
- SOCKS5: 207 alive / 83 gold

## Historical pool

- Discovered: 94324
- Ever alive: 9348
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
