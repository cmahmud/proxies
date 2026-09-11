# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 407
- HTTP: 88 alive / 68 gold
- HTTPS: 35 alive / 21 gold
- SOCKS4: 161 alive / 148 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48809
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
