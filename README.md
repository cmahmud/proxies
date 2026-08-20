# SyndProxy private pool

## Current pool

- Alive now: 806
- Gold now: 415
- HTTP: 205 alive / 84 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 212 alive / 156 gold
- SOCKS5: 224 alive / 155 gold

## Historical pool

- Discovered: 151073
- Ever alive: 27490
- Ever gold: 1098

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
