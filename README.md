# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 450
- HTTP: 132 alive / 83 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 208 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44781
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
