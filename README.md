# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 422
- HTTP: 100 alive / 70 gold
- HTTPS: 65 alive / 24 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47042
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
