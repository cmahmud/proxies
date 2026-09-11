# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 405
- HTTP: 94 alive / 68 gold
- HTTPS: 33 alive / 20 gold
- SOCKS4: 154 alive / 148 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48808
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
