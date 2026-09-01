# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 422
- HTTP: 94 alive / 67 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47063
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
