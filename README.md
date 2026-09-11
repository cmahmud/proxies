# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 404
- HTTP: 93 alive / 68 gold
- HTTPS: 34 alive / 20 gold
- SOCKS4: 154 alive / 148 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48808
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
