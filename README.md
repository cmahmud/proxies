# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 447
- HTTP: 144 alive / 78 gold
- HTTPS: 99 alive / 33 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 218 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45414
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
