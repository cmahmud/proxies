# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 379
- HTTP: 92 alive / 65 gold
- HTTPS: 40 alive / 25 gold
- SOCKS4: 158 alive / 118 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48730
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
