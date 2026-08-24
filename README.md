# SyndProxy validated proxy pool

## Current pool

- Alive now: 593
- Gold now: 432
- HTTP: 128 alive / 80 gold
- HTTPS: 107 alive / 23 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34041
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
