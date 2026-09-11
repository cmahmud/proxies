# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 405
- HTTP: 91 alive / 65 gold
- HTTPS: 30 alive / 20 gold
- SOCKS4: 158 alive / 146 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48798
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
