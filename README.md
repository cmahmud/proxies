# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 456
- HTTP: 130 alive / 84 gold
- HTTPS: 100 alive / 35 gold
- SOCKS4: 165 alive / 162 gold
- SOCKS5: 228 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45358
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
