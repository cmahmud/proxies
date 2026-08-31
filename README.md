# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 448
- HTTP: 131 alive / 78 gold
- HTTPS: 100 alive / 34 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 217 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45370
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
