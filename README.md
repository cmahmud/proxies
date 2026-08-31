# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 467
- HTTP: 153 alive / 96 gold
- HTTPS: 101 alive / 35 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45135
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
