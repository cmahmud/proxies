# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 474
- HTTP: 137 alive / 95 gold
- HTTPS: 118 alive / 39 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 202 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44888
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
