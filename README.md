# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 387
- HTTP: 111 alive / 68 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 181 alive / 154 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33246
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
