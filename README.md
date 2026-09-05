# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 274
- HTTP: 66 alive / 55 gold
- HTTPS: 54 alive / 21 gold
- SOCKS4: 187 alive / 65 gold
- SOCKS5: 260 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47764
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
