# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 491
- HTTP: 154 alive / 102 gold
- HTTPS: 146 alive / 50 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45002
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
