# SyndProxy private pool

## Current pool

- Alive now: 676
- Gold now: 345
- HTTP: 193 alive / 64 gold
- HTTPS: 99 alive / 14 gold
- SOCKS4: 195 alive / 135 gold
- SOCKS5: 189 alive / 132 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25789
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
