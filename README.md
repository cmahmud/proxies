# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 397
- HTTP: 101 alive / 72 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 179 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48097
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
