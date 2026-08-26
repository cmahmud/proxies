# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 404
- HTTP: 88 alive / 61 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39043
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
