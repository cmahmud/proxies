# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 400
- HTTP: 156 alive / 72 gold
- HTTPS: 63 alive / 14 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 195 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33287
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
