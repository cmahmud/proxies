# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 423
- HTTP: 96 alive / 67 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 190 alive / 168 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49072
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
