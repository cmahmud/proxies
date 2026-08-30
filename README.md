# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 464
- HTTP: 142 alive / 94 gold
- HTTPS: 110 alive / 36 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 208 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44856
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
