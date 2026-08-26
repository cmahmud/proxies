# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 400
- HTTP: 101 alive / 60 gold
- HTTPS: 88 alive / 14 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38342
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
