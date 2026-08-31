# SyndProxy validated proxy pool

## Current pool

- Alive now: 691
- Gold now: 458
- HTTP: 168 alive / 86 gold
- HTTPS: 112 alive / 36 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 234 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45328
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
