# SyndProxy validated proxy pool

## Current pool

- Alive now: 697
- Gold now: 456
- HTTP: 171 alive / 85 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 235 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45329
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
