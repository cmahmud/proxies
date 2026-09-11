# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 418
- HTTP: 90 alive / 65 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 193 alive / 168 gold
- SOCKS5: 182 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49069
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
