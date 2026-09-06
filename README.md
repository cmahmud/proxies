# SyndProxy validated proxy pool

## Current pool

- Alive now: 416
- Gold now: 317
- HTTP: 73 alive / 56 gold
- HTTPS: 30 alive / 5 gold
- SOCKS4: 147 alive / 134 gold
- SOCKS5: 166 alive / 122 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
