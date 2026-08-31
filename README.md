# SyndProxy validated proxy pool

## Current pool

- Alive now: 626
- Gold now: 474
- HTTP: 146 alive / 101 gold
- HTTPS: 111 alive / 37 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 193 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45124
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
