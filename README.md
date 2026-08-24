# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 391
- HTTP: 111 alive / 58 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33643
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
