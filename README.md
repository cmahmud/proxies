# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 304
- HTTP: 345 alive / 31 gold
- HTTPS: 208 alive / 4 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 211 alive / 127 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13440
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
