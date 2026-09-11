# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 407
- HTTP: 93 alive / 67 gold
- HTTPS: 31 alive / 21 gold
- SOCKS4: 161 alive / 146 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48788
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
