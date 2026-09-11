# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 371
- HTTP: 96 alive / 69 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 138 alive / 110 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48723
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
