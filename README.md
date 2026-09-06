# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 392
- HTTP: 95 alive / 66 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48242
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
