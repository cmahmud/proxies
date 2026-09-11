# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 423
- HTTP: 101 alive / 71 gold
- HTTPS: 52 alive / 23 gold
- SOCKS4: 185 alive / 165 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49032
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
