# SyndProxy private pool

## Current pool

- Alive now: 789
- Gold now: 336
- HTTP: 244 alive / 89 gold
- HTTPS: 162 alive / 20 gold
- SOCKS4: 190 alive / 129 gold
- SOCKS5: 193 alive / 98 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28945
- Ever gold: 1116

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
