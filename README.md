# SyndProxy private pool

## Current pool

- Alive now: 962
- Gold now: 356
- HTTP: 303 alive / 69 gold
- HTTPS: 196 alive / 18 gold
- SOCKS4: 247 alive / 154 gold
- SOCKS5: 216 alive / 115 gold

## Historical pool

- Discovered: 110865
- Ever alive: 15987
- Ever gold: 506

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
