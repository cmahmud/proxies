# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 403
- HTTP: 105 alive / 62 gold
- HTTPS: 92 alive / 11 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 203 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38242
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
