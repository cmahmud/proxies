# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 289
- HTTP: 351 alive / 27 gold
- HTTPS: 202 alive / 3 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 210 alive / 117 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13440
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
