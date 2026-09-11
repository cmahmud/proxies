# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 404
- HTTP: 90 alive / 65 gold
- HTTPS: 31 alive / 20 gold
- SOCKS4: 159 alive / 146 gold
- SOCKS5: 185 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48798
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
