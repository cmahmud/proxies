# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 386
- HTTP: 120 alive / 53 gold
- HTTPS: 68 alive / 12 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 162 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33380
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
