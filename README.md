# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 415
- HTTP: 102 alive / 68 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38007
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
