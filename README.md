# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 405
- HTTP: 79 alive / 62 gold
- HTTPS: 39 alive / 20 gold
- SOCKS4: 162 alive / 155 gold
- SOCKS5: 176 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48834
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
