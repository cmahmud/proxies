# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 467
- HTTP: 123 alive / 94 gold
- HTTPS: 129 alive / 36 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 217 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46463
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
