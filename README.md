# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 394
- HTTP: 89 alive / 66 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48134
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
