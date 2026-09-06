# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 393
- HTTP: 138 alive / 81 gold
- HTTPS: 53 alive / 21 gold
- SOCKS4: 154 alive / 138 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48027
- Ever gold: 1512

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
