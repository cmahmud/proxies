# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 322
- HTTP: 347 alive / 35 gold
- HTTPS: 220 alive / 10 gold
- SOCKS4: 214 alive / 149 gold
- SOCKS5: 231 alive / 128 gold

## Historical pool

- Discovered: 106888
- Ever alive: 14141
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
