# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 392
- HTTP: 143 alive / 56 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33641
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
