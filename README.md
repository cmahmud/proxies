# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 437
- HTTP: 112 alive / 88 gold
- HTTPS: 59 alive / 29 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49439
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
