# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 480
- HTTP: 153 alive / 105 gold
- HTTPS: 139 alive / 38 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
