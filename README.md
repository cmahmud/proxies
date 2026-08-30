# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 420
- HTTP: 128 alive / 82 gold
- HTTPS: 68 alive / 28 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 187 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44059
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
