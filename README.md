# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 481
- HTTP: 295 alive / 128 gold
- HTTPS: 234 alive / 83 gold
- SOCKS4: 201 alive / 129 gold
- SOCKS5: 228 alive / 141 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17562
- Ever gold: 675

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
