# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 432
- HTTP: 105 alive / 76 gold
- HTTPS: 56 alive / 26 gold
- SOCKS4: 189 alive / 169 gold
- SOCKS5: 176 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49093
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
