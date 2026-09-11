# SyndProxy validated proxy pool

## Current pool

- Alive now: 441
- Gold now: 358
- HTTP: 112 alive / 72 gold
- HTTPS: 50 alive / 21 gold
- SOCKS4: 100 alive / 95 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48700
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
