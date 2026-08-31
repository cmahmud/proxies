# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 479
- HTTP: 138 alive / 102 gold
- HTTPS: 129 alive / 42 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45059
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
