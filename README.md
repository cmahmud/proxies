# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 425
- HTTP: 134 alive / 82 gold
- HTTPS: 69 alive / 32 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 262 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43893
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
