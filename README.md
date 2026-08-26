# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 410
- HTTP: 109 alive / 66 gold
- HTTPS: 114 alive / 16 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38072
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
