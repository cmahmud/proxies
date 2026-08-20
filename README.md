# SyndProxy private pool

## Current pool

- Alive now: 1648
- Gold now: 590
- HTTP: 605 alive / 199 gold
- HTTPS: 487 alive / 100 gold
- SOCKS4: 252 alive / 139 gold
- SOCKS5: 304 alive / 152 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23361
- Ever gold: 918

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
