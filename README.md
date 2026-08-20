# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 389
- HTTP: 295 alive / 80 gold
- HTTPS: 209 alive / 26 gold
- SOCKS4: 201 alive / 131 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24940
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
