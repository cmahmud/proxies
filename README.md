# SyndProxy validated proxy pool

## Current pool

- Alive now: 414
- Gold now: 337
- HTTP: 85 alive / 63 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 147 alive / 136 gold
- SOCKS5: 144 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48362
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
