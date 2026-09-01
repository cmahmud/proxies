# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 459
- HTTP: 138 alive / 88 gold
- HTTPS: 128 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46864
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
