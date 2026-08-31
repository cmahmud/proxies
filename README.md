# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 445
- HTTP: 121 alive / 84 gold
- HTTPS: 87 alive / 28 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45649
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
