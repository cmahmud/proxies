# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 453
- HTTP: 132 alive / 88 gold
- HTTPS: 98 alive / 31 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 216 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45348
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
