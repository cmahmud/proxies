# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 441
- HTTP: 357 alive / 106 gold
- HTTPS: 283 alive / 35 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 244 alive / 164 gold

## Historical pool

- Discovered: 152761
- Ever alive: 28378
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
