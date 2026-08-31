# SyndProxy validated proxy pool

## Current pool

- Alive now: 700
- Gold now: 454
- HTTP: 162 alive / 86 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 239 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45340
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
