# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 314
- HTTP: 88 alive / 61 gold
- HTTPS: 36 alive / 22 gold
- SOCKS4: 116 alive / 102 gold
- SOCKS5: 142 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49512
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
