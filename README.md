# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 399
- HTTP: 109 alive / 68 gold
- HTTPS: 118 alive / 12 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33305
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
