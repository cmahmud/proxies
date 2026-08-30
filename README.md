# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 450
- HTTP: 131 alive / 83 gold
- HTTPS: 124 alive / 38 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 209 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44780
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
