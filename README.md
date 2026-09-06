# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 397
- HTTP: 112 alive / 75 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48076
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
