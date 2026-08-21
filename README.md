# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 394
- HTTP: 220 alive / 89 gold
- HTTPS: 158 alive / 21 gold
- SOCKS4: 215 alive / 129 gold
- SOCKS5: 228 alive / 155 gold

## Historical pool

- Discovered: 151688
- Ever alive: 27777
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
