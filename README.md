# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 373
- HTTP: 136 alive / 93 gold
- HTTPS: 40 alive / 31 gold
- SOCKS4: 92 alive / 74 gold
- SOCKS5: 233 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48645
- Ever gold: 1562

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
