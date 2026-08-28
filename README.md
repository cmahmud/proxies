# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 394
- HTTP: 79 alive / 58 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42818
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
