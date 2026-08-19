# SyndProxy private pool

## Current pool

- Alive now: 1219
- Gold now: 497
- HTTP: 446 alive / 164 gold
- HTTPS: 324 alive / 36 gold
- SOCKS4: 238 alive / 150 gold
- SOCKS5: 211 alive / 147 gold

## Historical pool

- Discovered: 125702
- Ever alive: 19683
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
