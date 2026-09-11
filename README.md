# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 427
- HTTP: 108 alive / 76 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 179 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48976
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
