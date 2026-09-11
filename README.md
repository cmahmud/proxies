# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 417
- HTTP: 83 alive / 64 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 190 alive / 163 gold
- SOCKS5: 182 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48885
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
