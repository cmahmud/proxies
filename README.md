# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 396
- HTTP: 110 alive / 60 gold
- HTTPS: 63 alive / 16 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 189 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33649
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
