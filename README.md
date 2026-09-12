# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 420
- HTTP: 104 alive / 76 gold
- HTTPS: 46 alive / 25 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49485
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
