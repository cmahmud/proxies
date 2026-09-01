# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 463
- HTTP: 139 alive / 93 gold
- HTTPS: 118 alive / 33 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46304
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
