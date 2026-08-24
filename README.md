# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 392
- HTTP: 109 alive / 59 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 172 alive / 156 gold
- SOCKS5: 193 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33520
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
