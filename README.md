# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 348
- HTTP: 76 alive / 64 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 140 alive / 135 gold
- SOCKS5: 161 alive / 136 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48410
- Ever gold: 1534

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
