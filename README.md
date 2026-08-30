# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 437
- HTTP: 105 alive / 80 gold
- HTTPS: 63 alive / 26 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44560
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
