# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 365
- HTTP: 82 alive / 42 gold
- HTTPS: 38 alive / 10 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 173050
- Ever alive: 32990
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
