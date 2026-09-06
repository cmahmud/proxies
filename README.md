# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 390
- HTTP: 101 alive / 70 gold
- HTTPS: 34 alive / 16 gold
- SOCKS4: 161 alive / 150 gold
- SOCKS5: 176 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48210
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
