# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 407
- HTTP: 94 alive / 68 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 162 alive / 147 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48810
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
