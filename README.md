# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 359
- HTTP: 114 alive / 36 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 192 alive / 156 gold

## Historical pool

- Discovered: 171584
- Ever alive: 32929
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
