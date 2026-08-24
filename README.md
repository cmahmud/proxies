# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 394
- HTTP: 96 alive / 58 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33352
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
