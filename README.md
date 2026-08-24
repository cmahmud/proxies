# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 387
- HTTP: 100 alive / 54 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33357
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
