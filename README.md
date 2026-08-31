# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 471
- HTTP: 148 alive / 97 gold
- HTTPS: 123 alive / 35 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 234 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46204
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
