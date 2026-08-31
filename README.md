# SyndProxy validated proxy pool

## Current pool

- Alive now: 582
- Gold now: 449
- HTTP: 113 alive / 86 gold
- HTTPS: 98 alive / 30 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45648
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
