# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 436
- HTTP: 321 alive / 95 gold
- HTTPS: 244 alive / 33 gold
- SOCKS4: 224 alive / 154 gold
- SOCKS5: 249 alive / 154 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30245
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
