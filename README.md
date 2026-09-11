# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 437
- HTTP: 108 alive / 77 gold
- HTTPS: 58 alive / 26 gold
- SOCKS4: 197 alive / 169 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49100
- Ever gold: 1573

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
