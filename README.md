# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 392
- HTTP: 98 alive / 57 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33352
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
