# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 472
- HTTP: 146 alive / 95 gold
- HTTPS: 129 alive / 41 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46937
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
