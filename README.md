# SyndProxy validated proxy pool

## Current pool

- Alive now: 425
- Gold now: 345
- HTTP: 77 alive / 63 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 153 alive / 137 gold
- SOCKS5: 163 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48398
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
