# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 403
- HTTP: 100 alive / 67 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 161 alive / 154 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43267
- Ever gold: 1368

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
