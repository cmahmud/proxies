# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 270
- HTTP: 202 alive / 32 gold
- HTTPS: 79 alive / 11 gold
- SOCKS4: 189 alive / 139 gold
- SOCKS5: 178 alive / 88 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9720
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
