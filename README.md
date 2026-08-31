# SyndProxy validated proxy pool

## Current pool

- Alive now: 696
- Gold now: 458
- HTTP: 160 alive / 89 gold
- HTTPS: 117 alive / 34 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 242 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45335
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
