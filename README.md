# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 371
- HTTP: 191 alive / 68 gold
- HTTPS: 145 alive / 17 gold
- SOCKS4: 192 alive / 144 gold
- SOCKS5: 216 alive / 142 gold

## Historical pool

- Discovered: 147648
- Ever alive: 25880
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
