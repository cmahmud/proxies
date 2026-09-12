# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 425
- HTTP: 97 alive / 76 gold
- HTTPS: 44 alive / 22 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49482
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
