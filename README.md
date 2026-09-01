# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 459
- HTTP: 143 alive / 88 gold
- HTTPS: 131 alive / 35 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46861
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
