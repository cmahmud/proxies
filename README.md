# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 393
- HTTP: 154 alive / 66 gold
- HTTPS: 66 alive / 14 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33287
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
