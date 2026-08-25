# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 400
- HTTP: 94 alive / 62 gold
- HTTPS: 85 alive / 19 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 169 alive / 159 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37636
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
