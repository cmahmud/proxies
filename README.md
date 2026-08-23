# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 332
- HTTP: 103 alive / 38 gold
- HTTPS: 84 alive / 5 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 185 alive / 137 gold

## Historical pool

- Discovered: 171581
- Ever alive: 32896
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
