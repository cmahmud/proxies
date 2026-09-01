# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 422
- HTTP: 102 alive / 69 gold
- HTTPS: 69 alive / 25 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47042
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
