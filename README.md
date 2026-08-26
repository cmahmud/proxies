# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 403
- HTTP: 101 alive / 61 gold
- HTTPS: 71 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39205
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
