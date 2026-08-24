# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 394
- HTTP: 100 alive / 60 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 184 alive / 159 gold
- SOCKS5: 197 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
