# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 431
- HTTP: 121 alive / 77 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33928
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
