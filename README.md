# SyndProxy validated proxy pool

## Current pool

- Alive now: 700
- Gold now: 347
- HTTP: 159 alive / 82 gold
- HTTPS: 109 alive / 39 gold
- SOCKS4: 101 alive / 53 gold
- SOCKS5: 331 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48554
- Ever gold: 1544

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
