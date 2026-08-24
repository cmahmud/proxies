# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 392
- HTTP: 110 alive / 57 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33647
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
