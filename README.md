# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 390
- HTTP: 124 alive / 66 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 202 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
