# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 421
- HTTP: 96 alive / 68 gold
- HTTPS: 67 alive / 25 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47030
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
