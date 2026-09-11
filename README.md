# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 423
- HTTP: 92 alive / 69 gold
- HTTPS: 67 alive / 25 gold
- SOCKS4: 188 alive / 165 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49062
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
