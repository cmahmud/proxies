# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 438
- HTTP: 111 alive / 77 gold
- HTTPS: 57 alive / 27 gold
- SOCKS4: 191 alive / 169 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49108
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
