# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 392
- HTTP: 95 alive / 66 gold
- HTTPS: 31 alive / 14 gold
- SOCKS4: 172 alive / 152 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48241
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
