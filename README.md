# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 318
- HTTP: 79 alive / 58 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 151 alive / 130 gold
- SOCKS5: 145 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48364
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
