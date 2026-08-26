# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 411
- HTTP: 98 alive / 62 gold
- HTTPS: 92 alive / 16 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 204 alive / 172 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38186
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
