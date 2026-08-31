# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 477
- HTTP: 150 alive / 97 gold
- HTTPS: 136 alive / 41 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 200 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45218
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
