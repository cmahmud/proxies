# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 361
- HTTP: 97 alive / 68 gold
- HTTPS: 52 alive / 23 gold
- SOCKS4: 125 alive / 101 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48714
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
