# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 481
- HTTP: 139 alive / 101 gold
- HTTPS: 121 alive / 43 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45073
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
