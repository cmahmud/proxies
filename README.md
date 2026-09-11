# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 366
- HTTP: 101 alive / 74 gold
- HTTPS: 69 alive / 33 gold
- SOCKS4: 300 alive / 79 gold
- SOCKS5: 229 alive / 180 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48585
- Ever gold: 1552

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
