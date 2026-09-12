# SyndProxy validated proxy pool

## Current pool

- Alive now: 388
- Gold now: 320
- HTTP: 84 alive / 66 gold
- HTTPS: 41 alive / 20 gold
- SOCKS4: 114 alive / 105 gold
- SOCKS5: 149 alive / 129 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49491
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
