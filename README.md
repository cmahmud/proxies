# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 459
- HTTP: 133 alive / 86 gold
- HTTPS: 131 alive / 35 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 194 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46826
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
