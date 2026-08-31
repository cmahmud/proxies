# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 441
- HTTP: 137 alive / 75 gold
- HTTPS: 99 alive / 33 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 202 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45373
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
