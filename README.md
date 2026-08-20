# SyndProxy private pool

## Current pool

- Alive now: 714
- Gold now: 351
- HTTP: 217 alive / 67 gold
- HTTPS: 125 alive / 19 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 179 alive / 135 gold

## Historical pool

- Discovered: 147175
- Ever alive: 25783
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
