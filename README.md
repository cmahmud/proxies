# SyndProxy validated proxy pool

## Current pool

- Alive now: 402
- Gold now: 341
- HTTP: 101 alive / 73 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 79 alive / 76 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48680
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
