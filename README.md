# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 370
- HTTP: 92 alive / 68 gold
- HTTPS: 48 alive / 22 gold
- SOCKS4: 139 alive / 111 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48724
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
