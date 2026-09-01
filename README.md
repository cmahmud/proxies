# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 454
- HTTP: 130 alive / 84 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46840
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
