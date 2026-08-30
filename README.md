# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 428
- HTTP: 121 alive / 87 gold
- HTTPS: 95 alive / 30 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 205 alive / 159 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44015
- Ever gold: 1388

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
