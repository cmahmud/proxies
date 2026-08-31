# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 461
- HTTP: 128 alive / 91 gold
- HTTPS: 139 alive / 33 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 233 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45784
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
