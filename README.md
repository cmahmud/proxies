# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 353
- HTTP: 67 alive / 53 gold
- HTTPS: 26 alive / 11 gold
- SOCKS4: 160 alive / 144 gold
- SOCKS5: 172 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48254
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
