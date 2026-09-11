# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 426
- HTTP: 95 alive / 64 gold
- HTTPS: 50 alive / 22 gold
- SOCKS4: 192 alive / 166 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48908
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
