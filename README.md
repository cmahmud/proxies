# SyndProxy validated proxy pool

## Current pool

- Alive now: 448
- Gold now: 368
- HTTP: 75 alive / 53 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48261
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
