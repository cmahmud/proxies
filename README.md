# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 301
- HTTP: 186 alive / 77 gold
- HTTPS: 142 alive / 36 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48488
- Ever gold: 1542

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
