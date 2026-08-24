# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 374
- HTTP: 118 alive / 55 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 189 alive / 154 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
