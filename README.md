# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 425
- HTTP: 99 alive / 74 gold
- HTTPS: 52 alive / 22 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49029
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
