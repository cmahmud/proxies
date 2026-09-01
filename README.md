# SyndProxy validated proxy pool

## Current pool

- Alive now: 597
- Gold now: 458
- HTTP: 133 alive / 89 gold
- HTTPS: 84 alive / 35 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 196 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46983
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
