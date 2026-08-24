# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 384
- HTTP: 112 alive / 58 gold
- HTTPS: 43 alive / 9 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
