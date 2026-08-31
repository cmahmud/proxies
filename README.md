# SyndProxy validated proxy pool

## Current pool

- Alive now: 650
- Gold now: 474
- HTTP: 158 alive / 102 gold
- HTTPS: 129 alive / 38 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45149
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
