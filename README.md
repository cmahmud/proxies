# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 430
- HTTP: 236 alive / 93 gold
- HTTPS: 222 alive / 21 gold
- SOCKS4: 224 alive / 154 gold
- SOCKS5: 260 alive / 162 gold

## Historical pool

- Discovered: 151677
- Ever alive: 27589
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
