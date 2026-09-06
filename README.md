# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 408
- HTTP: 110 alive / 79 gold
- HTTPS: 71 alive / 20 gold
- SOCKS4: 164 alive / 150 gold
- SOCKS5: 184 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48060
- Ever gold: 1517

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
