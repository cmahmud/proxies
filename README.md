# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 392
- HTTP: 157 alive / 65 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 192 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33287
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
