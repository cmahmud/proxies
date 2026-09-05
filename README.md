# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 274
- HTTP: 96 alive / 56 gold
- HTTPS: 45 alive / 20 gold
- SOCKS4: 153 alive / 65 gold
- SOCKS5: 252 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47774
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
