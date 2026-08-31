# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 474
- HTTP: 146 alive / 96 gold
- HTTPS: 107 alive / 39 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 204 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45109
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
