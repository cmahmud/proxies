# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 475
- HTTP: 133 alive / 97 gold
- HTTPS: 117 alive / 41 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44921
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
