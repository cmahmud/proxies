# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 426
- HTTP: 96 alive / 70 gold
- HTTPS: 61 alive / 26 gold
- SOCKS4: 185 alive / 167 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49056
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
