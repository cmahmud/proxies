# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 389
- HTTP: 110 alive / 57 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 161 gold

## Historical pool

- Discovered: 178284
- Ever alive: 33365
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
