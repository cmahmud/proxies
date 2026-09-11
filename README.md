# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 426
- HTTP: 92 alive / 72 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 201 alive / 168 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49086
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
