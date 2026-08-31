# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 420
- HTTP: 111 alive / 67 gold
- HTTPS: 75 alive / 22 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45519
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
