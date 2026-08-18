# SyndProxy private pool

## Current pool

- Alive now: 959
- Gold now: 347
- HTTP: 303 alive / 51 gold
- HTTPS: 190 alive / 15 gold
- SOCKS4: 231 alive / 141 gold
- SOCKS5: 235 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14686
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
