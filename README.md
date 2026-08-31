# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 452
- HTTP: 128 alive / 82 gold
- HTTPS: 104 alive / 35 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 216 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45363
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
