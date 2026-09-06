# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 411
- HTTP: 119 alive / 84 gold
- HTTPS: 70 alive / 22 gold
- SOCKS4: 170 alive / 146 gold
- SOCKS5: 182 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48053
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
