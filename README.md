# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 455
- HTTP: 132 alive / 84 gold
- HTTPS: 100 alive / 34 gold
- SOCKS4: 166 alive / 162 gold
- SOCKS5: 227 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45358
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
