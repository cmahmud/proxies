# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 381
- HTTP: 104 alive / 70 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 169 alive / 148 gold
- SOCKS5: 180 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48229
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
