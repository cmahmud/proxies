# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 536
- HTTP: 342 alive / 158 gold
- HTTPS: 244 alive / 88 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 216 alive / 141 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18075
- Ever gold: 714

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
