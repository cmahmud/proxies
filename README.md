# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 439
- HTTP: 111 alive / 82 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 195 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44564
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
