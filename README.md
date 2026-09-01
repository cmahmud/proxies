# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 459
- HTTP: 133 alive / 86 gold
- HTTPS: 132 alive / 36 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46827
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
