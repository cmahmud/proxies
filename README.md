# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 426
- HTTP: 96 alive / 71 gold
- HTTPS: 58 alive / 25 gold
- SOCKS4: 197 alive / 169 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49087
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
