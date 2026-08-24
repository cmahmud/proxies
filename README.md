# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 389
- HTTP: 111 alive / 55 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 180692
- Ever alive: 33646
- Ever gold: 1245

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
