# SyndProxy private pool

## Current pool

- Alive now: 719
- Gold now: 355
- HTTP: 227 alive / 66 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 187 alive / 132 gold
- SOCKS5: 179 alive / 137 gold

## Historical pool

- Discovered: 147175
- Ever alive: 25785
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
