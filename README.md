# SyndProxy validated proxy pool

## Current pool

- Alive now: 404
- Gold now: 315
- HTTP: 78 alive / 56 gold
- HTTPS: 36 alive / 6 gold
- SOCKS4: 146 alive / 132 gold
- SOCKS5: 144 alive / 121 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
