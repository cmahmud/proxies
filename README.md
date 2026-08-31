# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 456
- HTTP: 132 alive / 87 gold
- HTTPS: 103 alive / 33 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 215 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45348
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
