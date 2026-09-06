# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 319
- HTTP: 86 alive / 58 gold
- HTTPS: 34 alive / 12 gold
- SOCKS4: 144 alive / 133 gold
- SOCKS5: 146 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48371
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
