# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 283
- HTTP: 80 alive / 61 gold
- HTTPS: 236 alive / 34 gold
- SOCKS4: 53 alive / 52 gold
- SOCKS5: 138 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48469
- Ever gold: 1540

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
