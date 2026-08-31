# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 420
- HTTP: 84 alive / 61 gold
- HTTPS: 73 alive / 27 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
