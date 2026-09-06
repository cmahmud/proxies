# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 397
- HTTP: 102 alive / 73 gold
- HTTPS: 53 alive / 19 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 178 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48096
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
