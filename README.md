# SyndProxy validated proxy pool

## Current pool

- Alive now: 659
- Gold now: 479
- HTTP: 155 alive / 105 gold
- HTTPS: 138 alive / 38 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45230
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
