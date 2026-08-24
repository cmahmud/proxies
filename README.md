# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 396
- HTTP: 126 alive / 63 gold
- HTTPS: 57 alive / 11 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 190 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
