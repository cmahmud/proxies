# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 372
- HTTP: 135 alive / 80 gold
- HTTPS: 59 alive / 21 gold
- SOCKS4: 150 alive / 122 gold
- SOCKS5: 184 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48006
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
