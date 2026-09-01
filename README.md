# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 461
- HTTP: 133 alive / 94 gold
- HTTPS: 120 alive / 33 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 202 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46389
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
