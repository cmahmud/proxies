# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 394
- HTTP: 120 alive / 61 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 210 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
