# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 414
- HTTP: 242 alive / 86 gold
- HTTPS: 170 alive / 27 gold
- SOCKS4: 189 alive / 134 gold
- SOCKS5: 249 alive / 167 gold

## Historical pool

- Discovered: 162742
- Ever alive: 31468
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
