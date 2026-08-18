# SyndProxy private pool

## Current pool

- Alive now: 644
- Gold now: 239
- HTTP: 176 alive / 30 gold
- HTTPS: 71 alive / 9 gold
- SOCKS4: 196 alive / 111 gold
- SOCKS5: 201 alive / 89 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7596
- Ever gold: 339

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
