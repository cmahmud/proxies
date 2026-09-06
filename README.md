# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 354
- HTTP: 77 alive / 66 gold
- HTTPS: 33 alive / 14 gold
- SOCKS4: 152 alive / 137 gold
- SOCKS5: 165 alive / 137 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
