# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 404
- HTTP: 94 alive / 62 gold
- HTTPS: 70 alive / 16 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38491
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
