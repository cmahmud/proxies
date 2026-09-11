# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 377
- HTTP: 87 alive / 64 gold
- HTTPS: 45 alive / 24 gold
- SOCKS4: 145 alive / 119 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48733
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
