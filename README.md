# SyndProxy private pool

## Current pool

- Alive now: 1680
- Gold now: 636
- HTTP: 723 alive / 236 gold
- HTTPS: 535 alive / 133 gold
- SOCKS4: 184 alive / 103 gold
- SOCKS5: 238 alive / 164 gold

## Historical pool

- Discovered: 143423
- Ever alive: 24687
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
