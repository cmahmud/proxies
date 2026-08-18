# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 282
- HTTP: 336 alive / 29 gold
- HTTPS: 208 alive / 7 gold
- SOCKS4: 239 alive / 125 gold
- SOCKS5: 230 alive / 121 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13168
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
