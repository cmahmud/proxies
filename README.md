# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 479
- HTTP: 160 alive / 103 gold
- HTTPS: 128 alive / 40 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45247
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
