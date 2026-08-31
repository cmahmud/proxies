# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 449
- HTTP: 130 alive / 79 gold
- HTTPS: 102 alive / 34 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 218 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45366
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
