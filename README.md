# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 392
- HTTP: 117 alive / 60 gold
- HTTPS: 44 alive / 13 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 191 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33654
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
