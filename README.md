# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 448
- HTTP: 120 alive / 88 gold
- HTTPS: 50 alive / 31 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 176 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49296
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
