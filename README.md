# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 423
- HTTP: 101 alive / 72 gold
- HTTPS: 59 alive / 24 gold
- SOCKS4: 184 alive / 166 gold
- SOCKS5: 178 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49024
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
