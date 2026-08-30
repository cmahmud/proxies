# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 427
- HTTP: 114 alive / 77 gold
- HTTPS: 57 alive / 21 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44320
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
