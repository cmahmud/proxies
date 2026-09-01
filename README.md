# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 470
- HTTP: 140 alive / 95 gold
- HTTPS: 139 alive / 38 gold
- SOCKS4: 179 alive / 164 gold
- SOCKS5: 198 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46925
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
