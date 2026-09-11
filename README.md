# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 421
- HTTP: 90 alive / 69 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49062
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
