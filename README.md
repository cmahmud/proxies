# SyndProxy validated proxy pool

## Current pool

- Alive now: 719
- Gold now: 364
- HTTP: 103 alive / 74 gold
- HTTPS: 73 alive / 31 gold
- SOCKS4: 313 alive / 79 gold
- SOCKS5: 230 alive / 180 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1552

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
