# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 391
- HTTP: 125 alive / 61 gold
- HTTPS: 49 alive / 9 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
