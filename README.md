# SyndProxy validated proxy pool

## Current pool

- Alive now: 703
- Gold now: 461
- HTTP: 169 alive / 87 gold
- HTTPS: 124 alive / 37 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 236 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45325
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
