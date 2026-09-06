# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 394
- HTTP: 83 alive / 63 gold
- HTTPS: 35 alive / 15 gold
- SOCKS4: 182 alive / 155 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48147
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
