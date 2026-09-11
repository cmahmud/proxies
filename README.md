# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 451
- HTTP: 99 alive / 85 gold
- HTTPS: 49 alive / 30 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 189 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49190
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
