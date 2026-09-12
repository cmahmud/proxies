# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 317
- HTTP: 93 alive / 66 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 122 alive / 106 gold
- SOCKS5: 140 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49542
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
