# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 420
- HTTP: 127 alive / 81 gold
- HTTPS: 69 alive / 29 gold
- SOCKS4: 160 alive / 150 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44058
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
