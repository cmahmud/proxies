# SyndProxy validated proxy pool

## Current pool

- Alive now: 704
- Gold now: 459
- HTTP: 166 alive / 89 gold
- HTTPS: 118 alive / 34 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 239 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45335
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
