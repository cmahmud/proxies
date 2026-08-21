# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 446
- HTTP: 338 alive / 109 gold
- HTTPS: 285 alive / 34 gold
- SOCKS4: 209 alive / 152 gold
- SOCKS5: 249 alive / 151 gold

## Historical pool

- Discovered: 153725
- Ever alive: 28563
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
