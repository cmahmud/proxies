# SyndProxy validated proxy pool

## Current pool

- Alive now: 390
- Gold now: 315
- HTTP: 90 alive / 66 gold
- HTTPS: 32 alive / 17 gold
- SOCKS4: 122 alive / 105 gold
- SOCKS5: 146 alive / 127 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49526
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
