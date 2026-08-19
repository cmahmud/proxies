# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 519
- HTTP: 423 alive / 186 gold
- HTTPS: 315 alive / 53 gold
- SOCKS4: 196 alive / 121 gold
- SOCKS5: 236 alive / 159 gold

## Historical pool

- Discovered: 125606
- Ever alive: 19578
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
