# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 418
- HTTP: 98 alive / 66 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 179 alive / 166 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49018
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
