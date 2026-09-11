# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 426
- HTTP: 96 alive / 70 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 184 alive / 167 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49056
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
