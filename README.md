# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 458
- HTTP: 138 alive / 88 gold
- HTTPS: 134 alive / 35 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46857
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
