# SyndProxy validated proxy pool

## Current pool

- Alive now: 673
- Gold now: 491
- HTTP: 150 alive / 101 gold
- HTTPS: 149 alive / 51 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 204 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45002
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
