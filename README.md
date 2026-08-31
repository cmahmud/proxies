# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 468
- HTTP: 153 alive / 99 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 194 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45165
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
