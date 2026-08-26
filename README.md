# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 403
- HTTP: 103 alive / 60 gold
- HTTPS: 92 alive / 12 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 198 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38246
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
