# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 451
- HTTP: 126 alive / 82 gold
- HTTPS: 94 alive / 35 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 216 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45363
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
