# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 373
- HTTP: 340 alive / 90 gold
- HTTPS: 255 alive / 28 gold
- SOCKS4: 186 alive / 120 gold
- SOCKS5: 233 alive / 135 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28826
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
