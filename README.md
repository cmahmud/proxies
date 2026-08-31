# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 458
- HTTP: 110 alive / 91 gold
- HTTPS: 106 alive / 35 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45664
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
