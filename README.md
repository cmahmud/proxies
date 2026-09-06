# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 397
- HTTP: 110 alive / 70 gold
- HTTPS: 64 alive / 19 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 179 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48087
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
