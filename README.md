# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 435
- HTTP: 110 alive / 74 gold
- HTTPS: 55 alive / 28 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45553
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
