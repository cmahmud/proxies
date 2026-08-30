# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 426
- HTTP: 123 alive / 87 gold
- HTTPS: 83 alive / 31 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44072
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
