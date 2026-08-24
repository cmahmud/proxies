# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 391
- HTTP: 99 alive / 57 gold
- HTTPS: 48 alive / 11 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33351
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
