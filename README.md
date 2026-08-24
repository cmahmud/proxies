# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 391
- HTTP: 108 alive / 58 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 171 alive / 155 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33642
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
