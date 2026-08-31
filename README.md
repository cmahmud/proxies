# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 451
- HTTP: 161 alive / 89 gold
- HTTPS: 94 alive / 28 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 233 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45346
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
