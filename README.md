# SyndProxy private pool

## Current pool

- Alive now: 1464
- Gold now: 637
- HTTP: 543 alive / 236 gold
- HTTPS: 440 alive / 118 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 261 alive / 138 gold

## Historical pool

- Discovered: 142747
- Ever alive: 24630
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
