# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 431
- HTTP: 95 alive / 73 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47319
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
