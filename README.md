# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 357
- HTTP: 85 alive / 73 gold
- HTTPS: 55 alive / 32 gold
- SOCKS4: 144 alive / 75 gold
- SOCKS5: 201 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1556

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
