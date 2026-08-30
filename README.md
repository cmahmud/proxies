# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 445
- HTTP: 121 alive / 78 gold
- HTTPS: 136 alive / 36 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 199 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44694
- Ever gold: 1410

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
