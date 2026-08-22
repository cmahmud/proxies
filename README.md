# SyndProxy private pool

## Current pool

- Alive now: 751
- Gold now: 411
- HTTP: 190 alive / 85 gold
- HTTPS: 139 alive / 29 gold
- SOCKS4: 194 alive / 138 gold
- SOCKS5: 228 alive / 159 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31419
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
