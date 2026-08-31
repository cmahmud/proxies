# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 461
- HTTP: 120 alive / 90 gold
- HTTPS: 131 alive / 38 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45669
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
