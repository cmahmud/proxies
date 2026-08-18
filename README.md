# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 263
- HTTP: 269 alive / 27 gold
- HTTPS: 162 alive / 4 gold
- SOCKS4: 237 alive / 126 gold
- SOCKS5: 212 alive / 106 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12409
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
