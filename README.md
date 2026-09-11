# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 435
- HTTP: 106 alive / 76 gold
- HTTPS: 56 alive / 27 gold
- SOCKS4: 192 alive / 164 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49115
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
