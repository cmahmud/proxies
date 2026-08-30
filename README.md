# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 435
- HTTP: 105 alive / 80 gold
- HTTPS: 59 alive / 27 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 200 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44573
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
