# SyndProxy private pool

## Current pool

- Alive now: 1192
- Gold now: 531
- HTTP: 435 alive / 183 gold
- HTTPS: 329 alive / 81 gold
- SOCKS4: 217 alive / 127 gold
- SOCKS5: 211 alive / 140 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19778
- Ever gold: 797

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
