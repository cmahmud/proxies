# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 392
- HTTP: 91 alive / 64 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 182 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48151
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
