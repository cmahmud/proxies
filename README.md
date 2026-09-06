# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 392
- HTTP: 97 alive / 67 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48119
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
