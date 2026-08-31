# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 477
- HTTP: 170 alive / 103 gold
- HTTPS: 122 alive / 39 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45208
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
