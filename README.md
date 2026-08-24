# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 391
- HTTP: 113 alive / 56 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33645
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
