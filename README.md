# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 397
- HTTP: 116 alive / 73 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 180 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48084
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
