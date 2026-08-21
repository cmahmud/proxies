# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 436
- HTTP: 316 alive / 94 gold
- HTTPS: 244 alive / 34 gold
- SOCKS4: 219 alive / 155 gold
- SOCKS5: 254 alive / 153 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30246
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
