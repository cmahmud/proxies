# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 421
- HTTP: 115 alive / 70 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 204 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45521
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
