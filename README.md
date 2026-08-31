# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 456
- HTTP: 111 alive / 90 gold
- HTTPS: 110 alive / 34 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 195 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45664
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
