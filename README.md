# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 416
- HTTP: 244 alive / 95 gold
- HTTPS: 192 alive / 27 gold
- SOCKS4: 212 alive / 137 gold
- SOCKS5: 232 alive / 157 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27599
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
