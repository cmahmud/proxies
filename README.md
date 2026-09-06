# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 387
- HTTP: 90 alive / 66 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 178 alive / 154 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48123
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
