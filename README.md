# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 481
- HTTP: 139 alive / 103 gold
- HTTPS: 114 alive / 43 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45078
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
