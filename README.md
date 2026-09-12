# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 467
- HTTP: 141 alive / 96 gold
- HTTPS: 58 alive / 34 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49348
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
