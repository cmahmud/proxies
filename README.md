# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 459
- HTTP: 167 alive / 89 gold
- HTTPS: 119 alive / 34 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 236 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45334
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
