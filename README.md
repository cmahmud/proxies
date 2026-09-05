# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 284
- HTTP: 155 alive / 66 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 150 alive / 65 gold
- SOCKS5: 230 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47791
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
