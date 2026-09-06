# SyndProxy validated proxy pool

## Current pool

- Alive now: 442
- Gold now: 362
- HTTP: 73 alive / 50 gold
- HTTPS: 28 alive / 8 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 177 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48285
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
