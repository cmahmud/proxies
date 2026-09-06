# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 392
- HTTP: 95 alive / 65 gold
- HTTPS: 29 alive / 14 gold
- SOCKS4: 175 alive / 152 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48242
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
