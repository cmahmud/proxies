# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 406
- HTTP: 117 alive / 80 gold
- HTTPS: 70 alive / 17 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 182 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48067
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
