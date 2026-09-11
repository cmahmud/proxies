# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 382
- HTTP: 89 alive / 65 gold
- HTTPS: 44 alive / 21 gold
- SOCKS4: 156 alive / 125 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48741
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
