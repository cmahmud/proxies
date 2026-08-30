# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 439
- HTTP: 107 alive / 80 gold
- HTTPS: 59 alive / 28 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44570
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
