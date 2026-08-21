# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 416
- HTTP: 219 alive / 91 gold
- HTTPS: 164 alive / 25 gold
- SOCKS4: 224 alive / 139 gold
- SOCKS5: 220 alive / 161 gold

## Historical pool

- Discovered: 151686
- Ever alive: 27717
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
