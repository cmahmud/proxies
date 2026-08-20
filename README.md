# SyndProxy private pool

## Current pool

- Alive now: 731
- Gold now: 367
- HTTP: 178 alive / 69 gold
- HTTPS: 137 alive / 19 gold
- SOCKS4: 184 alive / 120 gold
- SOCKS5: 232 alive / 159 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26044
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
