# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 412
- HTTP: 97 alive / 66 gold
- HTTPS: 76 alive / 22 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37779
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
