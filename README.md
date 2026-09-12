# SyndProxy validated proxy pool

## Current pool

- Alive now: 394
- Gold now: 319
- HTTP: 86 alive / 65 gold
- HTTPS: 33 alive / 21 gold
- SOCKS4: 125 alive / 103 gold
- SOCKS5: 150 alive / 130 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49521
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
