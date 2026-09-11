# SyndProxy validated proxy pool

## Current pool

- Alive now: 723
- Gold now: 361
- HTTP: 105 alive / 75 gold
- HTTPS: 75 alive / 28 gold
- SOCKS4: 311 alive / 78 gold
- SOCKS5: 232 alive / 180 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1548

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
