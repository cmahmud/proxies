# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 394
- HTTP: 95 alive / 66 gold
- HTTPS: 34 alive / 18 gold
- SOCKS4: 161 alive / 138 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48779
- Ever gold: 1566

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
