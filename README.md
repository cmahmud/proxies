# SyndProxy validated proxy pool

## Current pool

- Alive now: 378
- Gold now: 292
- HTTP: 103 alive / 75 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 76 alive / 66 gold
- SOCKS5: 154 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47879
- Ever gold: 1500

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
