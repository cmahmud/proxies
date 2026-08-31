# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 422
- HTTP: 115 alive / 70 gold
- HTTPS: 69 alive / 23 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 196 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45522
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
