# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 447
- HTTP: 150 alive / 88 gold
- HTTPS: 81 alive / 35 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 217 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44216
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
