# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 304
- HTTP: 172 alive / 77 gold
- HTTPS: 30 alive / 15 gold
- SOCKS4: 82 alive / 73 gold
- SOCKS5: 173 alive / 139 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47820
- Ever gold: 1493

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
