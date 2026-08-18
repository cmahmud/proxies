# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 279
- HTTP: 434 alive / 31 gold
- HTTPS: 174 alive / 5 gold
- SOCKS4: 231 alive / 133 gold
- SOCKS5: 214 alive / 110 gold

## Historical pool

- Discovered: 99074
- Ever alive: 11377
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
