# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 405
- HTTP: 112 alive / 68 gold
- HTTPS: 164 alive / 14 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40956
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
