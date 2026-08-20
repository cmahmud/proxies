# SyndProxy private pool

## Current pool

- Alive now: 702
- Gold now: 379
- HTTP: 200 alive / 74 gold
- HTTPS: 104 alive / 18 gold
- SOCKS4: 198 alive / 144 gold
- SOCKS5: 200 alive / 143 gold

## Historical pool

- Discovered: 146130
- Ever alive: 25626
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
