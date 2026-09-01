# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 419
- HTTP: 90 alive / 68 gold
- HTTPS: 63 alive / 24 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47030
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
