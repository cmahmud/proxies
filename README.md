# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 369
- HTTP: 330 alive / 79 gold
- HTTPS: 238 alive / 25 gold
- SOCKS4: 212 alive / 137 gold
- SOCKS5: 243 alive / 128 gold

## Historical pool

- Discovered: 165837
- Ever alive: 32364
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
