# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 428
- HTTP: 136 alive / 75 gold
- HTTPS: 84 alive / 22 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33909
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
