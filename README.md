# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 362
- HTTP: 81 alive / 45 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48296
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
