# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 429
- HTTP: 335 alive / 89 gold
- HTTPS: 238 alive / 30 gold
- SOCKS4: 226 alive / 145 gold
- SOCKS5: 260 alive / 165 gold

## Historical pool

- Discovered: 158920
- Ever alive: 30136
- Ever gold: 1141

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
