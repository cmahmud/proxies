# SyndProxy private pool

## Current pool

- Alive now: 781
- Gold now: 396
- HTTP: 202 alive / 86 gold
- HTTPS: 128 alive / 26 gold
- SOCKS4: 215 alive / 135 gold
- SOCKS5: 236 alive / 149 gold

## Historical pool

- Discovered: 154727
- Ever alive: 29165
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
