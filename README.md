# SyndProxy private pool

## Current pool

- Alive now: 620
- Gold now: 384
- HTTP: 149 alive / 67 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 192 alive / 150 gold
- SOCKS5: 199 alive / 150 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25707
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
