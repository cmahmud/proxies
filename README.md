# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 415
- HTTP: 85 alive / 60 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36198
- Ever gold: 1269

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
