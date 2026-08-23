# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 391
- HTTP: 110 alive / 61 gold
- HTTPS: 78 alive / 15 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 189 alive / 160 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33145
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
