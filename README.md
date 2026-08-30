# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 429
- HTTP: 117 alive / 79 gold
- HTTPS: 60 alive / 22 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44535
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
