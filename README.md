# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 446
- HTTP: 120 alive / 77 gold
- HTTPS: 134 alive / 38 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 202 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44692
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
