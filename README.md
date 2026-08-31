# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 431
- HTTP: 105 alive / 73 gold
- HTTPS: 64 alive / 24 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 195 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45542
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
