# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 411
- HTTP: 88 alive / 60 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 190 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45516
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
