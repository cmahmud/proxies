# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 471
- HTTP: 151 alive / 99 gold
- HTTPS: 109 alive / 35 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45132
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
