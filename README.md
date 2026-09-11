# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 426
- HTTP: 105 alive / 67 gold
- HTTPS: 41 alive / 22 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48993
- Ever gold: 1570

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
