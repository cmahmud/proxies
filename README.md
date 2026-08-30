# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 446
- HTTP: 121 alive / 75 gold
- HTTPS: 142 alive / 41 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44676
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
