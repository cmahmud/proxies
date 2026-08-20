# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 352
- HTTP: 178 alive / 70 gold
- HTTPS: 104 alive / 14 gold
- SOCKS4: 182 alive / 134 gold
- SOCKS5: 184 alive / 134 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25788
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
