# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 405
- HTTP: 113 alive / 68 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 193 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33330
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
