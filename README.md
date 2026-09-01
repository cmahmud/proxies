# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 462
- HTTP: 134 alive / 86 gold
- HTTPS: 129 alive / 34 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 195 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46766
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
