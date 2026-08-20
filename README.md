# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 415
- HTTP: 243 alive / 97 gold
- HTTPS: 198 alive / 25 gold
- SOCKS4: 212 alive / 136 gold
- SOCKS5: 249 alive / 157 gold

## Historical pool

- Discovered: 151679
- Ever alive: 27598
- Ever gold: 1100

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
