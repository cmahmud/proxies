# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 416
- HTTP: 93 alive / 67 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47031
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
