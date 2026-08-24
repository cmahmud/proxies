# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 393
- HTTP: 113 alive / 60 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 206 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33339
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
