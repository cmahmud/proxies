# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 475
- HTTP: 136 alive / 101 gold
- HTTPS: 131 alive / 38 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45182
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
