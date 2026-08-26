# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 400
- HTTP: 111 alive / 62 gold
- HTTPS: 60 alive / 13 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38355
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
