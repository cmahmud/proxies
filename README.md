# SyndProxy private pool

## Current pool

- Alive now: 946
- Gold now: 368
- HTTP: 290 alive / 77 gold
- HTTPS: 249 alive / 28 gold
- SOCKS4: 180 alive / 123 gold
- SOCKS5: 227 alive / 140 gold

## Historical pool

- Discovered: 165755
- Ever alive: 32300
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
