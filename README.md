# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 355
- HTTP: 91 alive / 67 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 145 alive / 126 gold
- SOCKS5: 159 alive / 146 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49554
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
