# SyndProxy private pool

## Current pool

- Alive now: 683
- Gold now: 368
- HTTP: 158 alive / 69 gold
- HTTPS: 122 alive / 17 gold
- SOCKS4: 184 alive / 141 gold
- SOCKS5: 219 alive / 141 gold

## Historical pool

- Discovered: 147648
- Ever alive: 25875
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
