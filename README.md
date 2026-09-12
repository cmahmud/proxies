# SyndProxy validated proxy pool

## Current pool

- Alive now: 387
- Gold now: 326
- HTTP: 86 alive / 66 gold
- HTTPS: 33 alive / 20 gold
- SOCKS4: 128 alive / 111 gold
- SOCKS5: 140 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49547
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
