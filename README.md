# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 418
- HTTP: 123 alive / 76 gold
- HTTPS: 69 alive / 30 gold
- SOCKS4: 156 alive / 151 gold
- SOCKS5: 191 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44063
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
