# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 423
- HTTP: 91 alive / 70 gold
- HTTPS: 63 alive / 27 gold
- SOCKS4: 197 alive / 167 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49075
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
