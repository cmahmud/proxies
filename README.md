# SyndProxy private pool

## Current pool

- Alive now: 729
- Gold now: 356
- HTTP: 193 alive / 63 gold
- HTTPS: 117 alive / 19 gold
- SOCKS4: 210 alive / 132 gold
- SOCKS5: 209 alive / 142 gold

## Historical pool

- Discovered: 145551
- Ever alive: 25422
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
