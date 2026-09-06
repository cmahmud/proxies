# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 321
- HTTP: 81 alive / 59 gold
- HTTPS: 26 alive / 7 gold
- SOCKS4: 144 alive / 136 gold
- SOCKS5: 168 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48402
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
