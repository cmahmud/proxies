# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 358
- HTTP: 88 alive / 74 gold
- HTTPS: 55 alive / 32 gold
- SOCKS4: 161 alive / 75 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1556

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
