# SyndProxy private pool

## Current pool

- Alive now: 1263
- Gold now: 552
- HTTP: 450 alive / 178 gold
- HTTPS: 338 alive / 83 gold
- SOCKS4: 232 alive / 132 gold
- SOCKS5: 243 alive / 159 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22975
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
