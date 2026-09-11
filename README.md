# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 354
- HTTP: 84 alive / 74 gold
- HTTPS: 54 alive / 30 gold
- SOCKS4: 134 alive / 74 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1557

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
