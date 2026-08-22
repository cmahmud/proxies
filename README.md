# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 368
- HTTP: 325 alive / 79 gold
- HTTPS: 225 alive / 25 gold
- SOCKS4: 206 alive / 137 gold
- SOCKS5: 233 alive / 127 gold

## Historical pool

- Discovered: 165836
- Ever alive: 32363
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
