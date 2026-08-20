# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 393
- HTTP: 188 alive / 71 gold
- HTTPS: 168 alive / 14 gold
- SOCKS4: 213 alive / 159 gold
- SOCKS5: 212 alive / 149 gold

## Historical pool

- Discovered: 147653
- Ever alive: 25888
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
