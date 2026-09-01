# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 454
- HTTP: 127 alive / 88 gold
- HTTPS: 116 alive / 29 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46733
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
