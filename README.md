# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 442
- HTTP: 117 alive / 80 gold
- HTTPS: 93 alive / 32 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44626
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
