# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 454
- HTTP: 127 alive / 84 gold
- HTTPS: 94 alive / 36 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 218 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45354
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
