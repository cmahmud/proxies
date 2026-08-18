# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 282
- HTTP: 309 alive / 27 gold
- HTTPS: 201 alive / 4 gold
- SOCKS4: 226 alive / 134 gold
- SOCKS5: 246 alive / 117 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12744
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
