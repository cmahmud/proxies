# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 333
- HTTP: 277 alive / 56 gold
- HTTPS: 172 alive / 14 gold
- SOCKS4: 201 alive / 132 gold
- SOCKS5: 194 alive / 131 gold

## Historical pool

- Discovered: 127417
- Ever alive: 19990
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
