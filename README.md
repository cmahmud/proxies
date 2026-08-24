# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 429
- HTTP: 134 alive / 76 gold
- HTTPS: 74 alive / 22 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33910
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
