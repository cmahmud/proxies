# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 443
- HTTP: 143 alive / 79 gold
- HTTPS: 111 alive / 29 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 213 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45430
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
