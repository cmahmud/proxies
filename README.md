# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 366
- HTTP: 415 alive / 78 gold
- HTTPS: 243 alive / 25 gold
- SOCKS4: 220 alive / 135 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32360
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
