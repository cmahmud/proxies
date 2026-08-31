# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 457
- HTTP: 130 alive / 86 gold
- HTTPS: 116 alive / 36 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45620
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
