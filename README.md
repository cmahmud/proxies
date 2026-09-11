# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 373
- HTTP: 158 alive / 91 gold
- HTTPS: 41 alive / 30 gold
- SOCKS4: 95 alive / 75 gold
- SOCKS5: 224 alive / 177 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48644
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
