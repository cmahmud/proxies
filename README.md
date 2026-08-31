# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 474
- HTTP: 155 alive / 103 gold
- HTTPS: 130 alive / 36 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45197
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
