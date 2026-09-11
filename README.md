# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 387
- HTTP: 94 alive / 65 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 169 alive / 130 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48750
- Ever gold: 1565

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
