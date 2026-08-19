# SyndProxy private pool

## Current pool

- Alive now: 1231
- Gold now: 534
- HTTP: 458 alive / 185 gold
- HTTPS: 336 alive / 79 gold
- SOCKS4: 225 alive / 130 gold
- SOCKS5: 212 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19792
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
