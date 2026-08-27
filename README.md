# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 426
- HTTP: 103 alive / 80 gold
- HTTPS: 100 alive / 20 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42095
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
